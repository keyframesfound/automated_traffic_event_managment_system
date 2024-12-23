import cv2
import torch
import easyocr
import yolov5
import numpy as np
import json

def list_available_cameras():
    """Lists all available camera indices until no camera is found."""
    available_cameras = []
    index = 0
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        available_cameras.append(index)
        cap.release()
        index += 1
    return available_cameras

def select_camera():
    """Prompts user to select a camera from available options."""
    available_cameras = list_available_cameras()
    
    if not available_cameras:
        print("No cameras found!")
        return None
    
    print("\nAvailable cameras:")
    for idx in available_cameras:
        print(f"Camera {idx}")
    
    while True:
        try:
            selection = int(input("\nSelect camera number: "))
            if selection in available_cameras:
                return selection
            print("Invalid camera number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def put_text_with_background(img, text, position, font, font_scale, text_color, thickness):
    """Puts text on image with a semi-transparent background."""
    (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)
    
    # Create background rectangle coordinates
    padding = 10
    bg_rect_start = (position[0] - padding, position[1] - text_height - padding)
    bg_rect_end = (position[0] + text_width + padding, position[1] + padding)
    
    # Create semi-transparent overlay
    overlay = img.copy()
    cv2.rectangle(overlay, bg_rect_start, bg_rect_end, (0, 0, 0), -1)
    
    # Apply transparency
    alpha = 0.6
    img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)
    
    # Add text
    cv2.putText(img, text, position, font, font_scale, text_color, thickness)
    return img

# Load authorized plates from JSON file
with open('data.json', 'r') as file:
    config = json.load(file)
    authorized_plates = config.get("authorized_plates", [])

model = yolov5.load('keremberke/yolov5m-license-plate')
reader = easyocr.Reader(['en'])
confidence_threshold = 0.5

# Camera selection
camera_index = select_camera()
if camera_index is None:
    print("Exiting due to no available cameras.")
    exit()

cap = cv2.VideoCapture(camera_index)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    frame_resized = cv2.resize(frame, (640, 480))
    results = model(frame_resized)
    detections = results.xyxy[0].numpy()

    for detection in detections:
        x1, y1, x2, y2, conf, cls = detection
        if conf > confidence_threshold:
            x1_orig = int(x1 * (w / 640))
            y1_orig = int(y1 * (h / 480))
            x2_orig = int(x2 * (w / 640))
            y2_orig = int(y2 * (h / 480))

            cv2.rectangle(frame, (x1_orig, y1_orig), (x2_orig, y2_orig), (0, 255, 0), 8)
            license_plate = frame[y1_orig:y2_orig, x1_orig:x2_orig]
            result = reader.readtext(license_plate, paragraph=False)
            license_plate_text = ''.join([line[1].upper().replace(" ", "") for line in result])

            is_authorized = any(
                sum(1 for char in plate if char in license_plate_text) == len(plate)
                for plate in authorized_plates
            )

            text_color = (0, 255, 0) if is_authorized else (0, 0, 255)
            status_text = "Authorized" if is_authorized else "Not Authorized"

            frame = put_text_with_background(frame, f"Plate: {license_plate_text}", (x1_orig, y1_orig - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, text_color, 2)
            frame = put_text_with_background(frame, status_text, (x1_orig, y1_orig - 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, text_color, 2)

    cv2.imshow("License Plate Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()