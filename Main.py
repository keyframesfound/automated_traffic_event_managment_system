import cv2
import torch
import time
import easyocr

# Load the YOLOv5 model
model = torch.hub.load("ultralytics/yolov5", "yolov5s")

# Prompt the user to select the camera index
camera_index = int(input("Enter the camera index (e.g., 0 for the default camera): "))

# Initialize the camera
cap = cv2.VideoCapture(camera_index)

# Read the authorized license plates
authorized_plates = ["LICENSE", "LICENSE", "LICENSE"]

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])

running = True
frame_count = 0
start_time = time.time()
prev_time = start_time
fps = 0.0  # Initialize the fps variable

# Set the confidence threshold
confidence_threshold = 0.25  # Set a lower confidence threshold

while running:
    # Capture a single frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # Get original frame dimensions
    h, w, _ = frame.shape

    # Resize the frame to a smaller size for inference
    frame_resized = cv2.resize(frame, (640, 480))  # Use a size suitable for YOLOv5

    # Perform inference
    results = model(frame_resized)

    # Process the inference results
    detections = results.xyxy[0].numpy()  # Get detections in numpy array format

    for detection in detections:
        x1, y1, x2, y2, conf, cls = detection  # Unpack detection results
        if conf > confidence_threshold:  # Use the modified confidence threshold
            # Rescale bounding box coordinates to the original frame dimensions
            x1_orig = int(x1 * (w / 640))
            y1_orig = int(y1 * (h / 480))
            x2_orig = int(x2 * (w / 640))
            y2_orig = int(y2 * (h / 480))

            # Draw the bounding box on the original frame
            cv2.rectangle(frame, (x1_orig, y1_orig), (x2_orig, y2_orig), (0, 255, 0), 2)

            # Extract the license plate region from the original frame
            license_plate = frame[y1_orig:y2_orig, x1_orig:x2_orig]

            # Perform OCR on the license plate region using EasyOCR
            result = reader.readtext(license_plate, paragraph=False)
            license_plate_text = ''.join([line[1].upper().replace(" ", "") for line in result])

            # Check if the license plate contains at least 4 out of the 5 characters in any of the authorized plates
            is_authorized = any(
                sum(1 for char in authorized_plate if char in license_plate_text) >= 4 for authorized_plate in authorized_plates
            )

            # Determine the gate status based on the authorization
            gate_status = "Authorized" if is_authorized else "Guest Car"
            color = (0, 255, 0) if is_authorized else (0, 0, 255)  # Green for authorized, Red for guest

            # Draw the license plate text and gate status on the frame
            cv2.putText(frame, license_plate_text, (x1_orig, y1_orig - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            cv2.putText(frame, gate_status, (x1_orig, y1_orig - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

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
    cv2.putText(frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the processed frame
    cv2.imshow("License Plate Detection", frame)

    # Check for user input
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        running = False

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()