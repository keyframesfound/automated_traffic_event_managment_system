from roboflow import Roboflow
import cv2
from concurrent.futures import ThreadPoolExecutor
import pytesseract
import time

# Prompt the user to select the camera index
camera_index = int(input("Enter the camera index (e.g., 0 for the default camera): "))

# Initialize the camera
cap = cv2.VideoCapture(camera_index)

# Set up Roboflow
rf = Roboflow(api_key="u7DLC0ZfVDyLXmbYFpQI")
project = rf.workspace().project("license-plate-recognition-rxg4e")
model = project.version("4").model  # Use the higher-resolution model version

# Set up the thread pool for asynchronous API calls
executor = ThreadPoolExecutor(max_workers=2)

# Read the authorized license plates from a CSV file
authorized_plates = ["LICENSE123", "ABC123", "DEF456"]

running = True
frame_count = 0
start_time = time.time()
prev_time = start_time
fps = 0.0  # Initialize the fps variable

while running:
    # Capture a single frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    try:
        results = model.predict(frame, confidence=0.7, overlap=0.4)
        detections = results.json()['predictions']
    except Exception as e:
        print(f"Error: {e}")
        continue

    # Process the inference results
    for detection in detections:
        x1, y1, x2, y2 = detection['x'], detection['y'], detection['width'] + detection['x'], detection['height'] + detection['y']

        # Calculate the aspect ratio of a typical license plate (approximately 3:1)
        plate_width = x2 - x1
        plate_height = plate_width / 3

        # Adjust the bounding box coordinates to better fit the license plate region
        x1 = max(0, int(x1 - 0.4 * plate_width))
        y1 = max(0, int(y1 - 0.5 * plate_height))
        x2 = min(frame.shape[1], int(x2 + 0.2 * plate_width))
        y2 = min(frame.shape[0], int(y1 + 1.2 * plate_height))

        # Extract the license plate region
        license_plate = frame[int(y1):int(y2), int(x1):int(x2)]

        try:
            # Perform OCR on the license plate region using Tesseract
            license_plate_text = pytesseract.image_to_string(license_plate, config='--oem 3 --psm 6')
            license_plate_text = license_plate_text.strip().upper().replace(" ", "")

            # Check if the license plate contains at least 4 out of the 5 characters in any of the authorized plates (ignoring '?' characters)
            is_authorized = any(sum(1 for char in authorized_plate if char != '?' and char in license_plate_text.replace('?', '')) >= 4 for authorized_plate in authorized_plates)

            # Determine the gate status based on the authorization
            if is_authorized:
                gate_status = "Authorized"
                color = (0, 255, 0)  # Green
            else:
                gate_status = "Guest Car"
                color = (0, 0, 255)  # Red

            # Draw the bounding box, license plate text, and gate status on the frame
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 5)
            text_x = int(x1)
            text_y = int(y1) - 60
            text_bg_height = 60
            text_bg_width = max(cv2.getTextSize(license_plate_text, cv2.FONT_HERSHEY_SIMPLEX, 2, 5)[0][0],
                               cv2.getTextSize(gate_status, cv2.FONT_HERSHEY_SIMPLEX, 2, 5)[0][0]) + 20
            text_bg_x1 = int(x1)
            text_bg_y1 = int(y1) - text_bg_height
            text_bg_x2 = int(x1) + text_bg_width
            text_bg_y2 = int(y1)
            cv2.rectangle(frame, (text_bg_x1, text_bg_y1), (text_bg_x2, text_bg_y2), color, -1)
            cv2.putText(frame, license_plate_text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)
            text_y += 50
            cv2.putText(frame, gate_status, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)
        except Exception as e:
            print(f"Error processing license plate: {e}")
            continue

    # Calculate the current FPS
    frame_count += 1
    current_time = time.time()
    elapsed_time = current_time - prev_time
    if elapsed_time >= 1:  # Update FPS every second
        fps = frame_count / elapsed_time
        frame_count = 0
        prev_time = current_time

    # Display the FPS
    fps_text = f"FPS: {fps:.2f}"
    cv2.putText(frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    # Display the processed frame
    cv2.imshow("License Plate Detection", frame)

    # Check for user input
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        running = False

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()