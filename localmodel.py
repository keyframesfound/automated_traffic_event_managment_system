import cv2
import pytesseract

# Load the license plate detection model
net = cv2.dnn.readNetFromONNX('/Users/ryanyeung/miniconda3/pkgs/libopencv-4.10.0-headless_py38h1ed5c01_3/share/opencv4/haarcascades/haarcascade_license_plate_rus_16stages.xml')

# Function to detect and read license plate
def read_license_plate(frame):
    # Create a blob from the frame
    blob = cv2.dnn.blobFromImage(frame, scalefactor=1/255.0, size=(224, 224), mean=(0, 0, 0), swapRB=True, crop=False)

    # Pass the blob through the license plate detection model
    net.setInput(blob)
    outputs = net.forward()

    # Extract the license plate region
    for output in outputs:
        x, y, width, height = output[:4]
        x, y, width, height = int(x * frame.shape[1]), int(y * frame.shape[0]), int(width * frame.shape[1]), int(height * frame.shape[0])
        plate_region = frame[y:y+height, x:x+width]

        # Use Tesseract OCR to read the license plate
        text = pytesseract.image_to_string(plate_region, lang='eng', config='--psm 6')

        # Extract the license plate number
        license_plate = ''.join(char for char in text if char.isalnum())

        if license_plate:
            return license_plate

    return None

# Function to get camera source
def get_camera_source():
    # (Same as before)

# Main function
def main():
    # Get camera source
    camera_source = get_camera_source()

    # Open the camera or video source
    cap = cv2.VideoCapture(camera_source)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        if ret:
            # Detect and read the license plate
            license_plate = read_license_plate(frame)

            if license_plate:
                # Display the license plate number
                print("License plate:", license_plate)

            # Display the frame
            cv2.imshow("License Plate Recognition", frame)

            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()