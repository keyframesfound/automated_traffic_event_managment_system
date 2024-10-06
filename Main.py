import cv2
from inference_sdk import InferenceHTTPClient
import time
from concurrent.futures import ThreadPoolExecutor
import pytesseract
import csv

# Prompt the user to select the camera index
camera_index = int(input("Enter the camera index (e.g., 0 for the default camera): "))

# Initialize the camera
cap = cv2.VideoCapture(camera_index)

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="API Key"
)

# Set up the thread pool for asynchronous API calls
executor = ThreadPoolExecutor(max_workers=8)

# Read the authorized license plates from a CSV file
authorized_plates = ["License", "License", "License", "License", "License", "License]

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

    # Submit the frame for inference in the background
    future = executor.submit(CLIENT.infer, frame, model_id="license-plate-recognition-rxg4e/4")
    response = future.result()

    # Process the inference results
    detections = response.get("predictions", [])
    for detection in detections:
        x, y, width, height = detection["x"], detection["y"], detection["width"], detection["height"]
        x1, y1 = int(x - width / 2), int(y - height / 2)
        x2, y2 = int(x + width / 2), int(y + height / 2)
        confidence = detection["confidence"]
        label = detection["class"]

        # Draw the bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

        # Extract the license plate region
        license_plate = frame[y1:y2, x1:x2]

        # Perform OCR on the license plate region
        license_plate_text = pytesseract.image_to_string(license_plate, config='--oem 3 --psm 6')
        license_plate_text = license_plate_text.strip().upper().replace(" ", "")

        # Check if the license plate contains at least 4 out of the 5 characters in any of the authorized plates
        is_authorized = any(sum(1 for char in authorized_plate if char in license_plate_text) >= 4 for authorized_plate in authorized_plates)

        # Determine the gate status based on the authorization
        if is_authorized:
            gate_status = "Authorized"
            color = (0, 255, 0)  # Green
        else:
            gate_status = "Guest Car"
            color = (0, 0, 255)  # Red

        # Draw the license plate text and gate status on the frame
        text_x = x1
        text_y = y1 - 60
        text_bg_height = 60
        text_bg_width = max(cv2.getTextSize(license_plate_text, cv2.FONT_HERSHEY_SIMPLEX, 2, 5)[0][0],
                           cv2.getTextSize(gate_status, cv2.FONT_HERSHEY_SIMPLEX, 2, 5)[0][0]) + 20
        text_bg_x1 = x1
        text_bg_y1 = y1 - text_bg_height
        text_bg_x2 = x1 + text_bg_width
        text_bg_y2 = y1
        cv2.rectangle(frame, (text_bg_x1, text_bg_y1), (text_bg_x2, text_bg_y2), color, -1)
        cv2.putText(frame, license_plate_text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)
        text_y += 50
        cv2.putText(frame, gate_status, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)

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