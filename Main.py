import cv2
from inference_sdk import InferenceHTTPClient
import time
from concurrent.futures import ThreadPoolExecutor
import easyocr

# Prompt the user to select the camera index
camera_index = int(input("Enter the camera index (e.g., 0 for the default camera): "))

# Initialize the camera
cap = cv2.VideoCapture(camera_index)

# Set the camera frame rate to 5 FPS
cap.set(cv2.CAP_PROP_FPS, 5)

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="u7DLC0ZfVDyLXmbYFpQI"
)

# Set up the thread pool for asynchronous API calls
executor = ThreadPoolExecutor(max_workers=1)

# Read the authorized license plates
authorized_plates = ["DF8588", "EC412", "LICENSE"]

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])

running = True
frame_count = 0
start_time = time.time()
prev_time = start_time
fps = 0.0  # Initialize the fps variable
last_processed_time = time.time()
skip_frames = 2  # Process every 3rd frame

while running:
    # Capture a single frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # Resize the frame to a smaller size
    frame = cv2.resize(frame, (320, 180))  # Reduced resolution

    # Check if it's time to process the frame
    if fps > 0 and time.time() - last_processed_time > 1 / fps / (skip_frames + 1):
        # Submit the frame for inference in the background
        future = executor.submit(CLIENT.infer, frame, model_id="license-plate-recognition-rxg4e/4")
        response = future.result()

        # Process the inference results
        # (rest of the code remains the same)

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
