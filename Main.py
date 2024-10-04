import cv2
from inference_sdk import InferenceHTTPClient
import time

# Prompt the user to select the camera source
camera_index = int(input("Enter the camera index (e.g., 0 for the default camera): "))

# Initialize the camera
cap = cv2.VideoCapture(camera_index)

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="API KEY"
)

running = True
prev_time = 0
while running:
    # Capture a frame from the camera
    ret, frame = cap.read()

    if ret:
        # Perform object detection on the frame
        response = CLIENT.infer(frame, model_id="license-plate-recognition-rxg4e/4")
        
        # Extract the detections from the response
        detections = response.get("predictions", [])

        # Calculate the current FPS
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time

        # Draw bounding boxes, display confidence scores, and FPS
        for detection in detections:
            x, y, w, h = detection["x"], detection["y"], detection["width"], detection["height"]
            class_id = detection["class_id"]
            confidence = detection["confidence"] * 100
            
            # Lookup the class name based on the class_id
            class_names = {0: "License Plate"}
            label = class_names.get(class_id, "Unknown")
            
            # Adjust the bounding box coordinates to center it on the detection
            x = int(x - w / 2)
            y = int(y - h / 2)
            w = int(w)
            h = int(h)
            
            # Draw the bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Display the label and confidence score
            text = f"{label}: {confidence:.2f}%"
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Display the FPS
        fps_text = f"FPS: {fps:.2f}"
        cv2.putText(frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # Display the frame
        cv2.imshow("License Plate Detection", frame)

        # Check for user input
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            running = False

    # Limit the frame rate to improve performance
    time.sleep(0.01)

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()