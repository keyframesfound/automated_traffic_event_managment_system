import cv2
import numpy as np
import pytesseract
import os
from datetime import datetime

# Function to get the available camera sources
def get_camera_sources():
    camera_sources = []
    for i in range(10):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            camera_sources.append(i)
            cap.release()
    return camera_sources

# Function to start the license plate detection and reading
def start_license_plate_detection(camera_source, record_video):
    plat_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")
    video = cv2.VideoCapture(camera_source)

    if not video.isOpened():
        print('Error Reading Video')
        return

    if record_video:
        # Create a directory to save the recorded videos
        output_dir = "license_plate_videos"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Get the current date and time
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        video_filename = os.path.join(output_dir, f"license_plate_video_{date_time}.mp4")

        # Create the video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(video_filename, fourcc, 20.0, (int(video.get(3)), int(video.get(4))))

    while True:
        ret, frame = video.read()
        gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        plate = plat_detector.detectMultiScale(gray_video, scaleFactor=1.2, minNeighbors=5, minSize=(25, 25))

        for (x, y, w, h) in plate:
            license_plate = frame[y:y + h, x:x + w]
            license_plate_text = pytesseract.image_to_string(license_plate, lang='eng')
            license_plate_text = ''.join(c for c in license_plate_text if c.isalnum())

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            frame[y:y + h, x:x + w] = cv2.blur(frame[y:y + h, x:x + w], ksize=(10, 10))
            cv2.putText(frame, text=license_plate_text, org=(x - 3, y - 3), fontFace=cv2.FONT_HERSHEY_COMPLEX, color=(0, 0, 255), thickness=1, fontScale=0.6)

        if ret == True:
            if record_video:
                out.write(frame)
            cv2.imshow('Video', frame)

            if cv2.waitKey(25) & 0xFF == ord("q"):
                break
        else:
            break

    video.release()
    if record_video:
        out.release()
    cv2.destroyAllWindows()

# Main function
if __name__ == "__main__":
    # Install Tesseract OCR engine
    pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

    # Get the available camera sources
    camera_sources = get_camera_sources()
    print("Available camera sources:", camera_sources)

    # Prompt the user to choose a camera source
    camera_choice = int(input("Enter the camera source number (0-{})?: ".format(len(camera_sources) - 1)))

    # Prompt the user to choose whether to record the video or not
    record_video = input("Do you want to record the video? (yes/no): ").lower() == "yes"

    # Start the license plate detection and reading
    start_license_plate_detection(camera_sources[camera_choice], record_video)