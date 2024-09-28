import cv2
import numpy as np
from ultralytics import YOLO
import pytesseract
import threading

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# Initialize the video capture
cap = cv2.VideoCapture(0)

def recognize_number_plate(img):
    """
    Recognize the license plate number from the input image using Tesseract OCR.
    """
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply image preprocessing (e.g., thresholding, noise removal)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    
    # Use Tesseract OCR to extract the license plate number
    license_plate = pytesseract.image_to_string(thresh, lang='eng', config='--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    # Clean up the extracted text
    license_plate = ''.join(c for c in license_plate if c.isalnum())
    return license_plate.upper()

def process_frame(frame):
    # Perform object detection using YOLOv8
    results = model(frame)[0]
    
    # Iterate over the detected objects
    for result in results.boxes.data:
        # Get the bounding box coordinates
        x1, y1, x2, y2 = int(result[0]), int(result[1]), int(result[2]), int(result[3])
        
        # Get the class ID and confidence score
        class_id = int(result[5])
        confidence = result[4]
        
        # Check if the detected object is a car
        if class_id == 2:  # Car class ID
            # Crop the number plate region
            number_plate = frame[y1:y2, x1:x2]
            
            # Perform number plate recognition
            license_plate = recognize_number_plate(number_plate)
            
            # Draw the bounding box and display the license plate
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, license_plate, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12), 2)
    
    return frame

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()
    
    # Process the frame using a separate thread
    thread = threading.Thread(target=process_frame, args=(frame,))
    thread.start()
    thread.join()
    
    # Display the frame
    cv2.imshow('Car Number Plate Recognition', frame)
    
    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
