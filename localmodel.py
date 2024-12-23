import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
import json
import cv2
import easyocr
from datetime import datetime
import random

# Initialize EasyOCR
reader = easyocr.Reader(['en'], gpu=False)

# Initialize camera
cam = cv2.VideoCapture(0)
cv2.namedWindow("cam")

# Constants
threshold = 0.25
DATA_FILE = 'data.json'

def init_database():
    """Initialize the database file if it doesn't exist"""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)

def getRandomCharge():
    """Generate random parking charge"""
    charges = [100, 200, 300, 400, 500]
    return charges[random.randint(0, len(charges) - 1)]

def load_data():
    """Load data from JSON file"""
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    """Save data to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def check(vehicleNo, score):
    """Check vehicle and manage database"""
    if vehicleNo.startswith('MH') and len(vehicleNo) >= 8:
        data = load_data()

        # Check if vehicle exists
        existing_vehicle = None
        for entry in data:
            if entry['vehicleNo'] == vehicleNo:
                existing_vehicle = entry
                break

        if not existing_vehicle:
            print("New vehicle. Adding to database:", vehicleNo, score)
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            charge = getRandomCharge()
            new_entry = {
                'vehicleNo': vehicleNo,
                'time': now,
                'charge': charge,
                'paid': False
            }
            data.append(new_entry)
            save_data(data)
            return False
        else:
            print("Vehicle already in database")
            return True

    return False

def start_cam():
    """Main camera loop"""
    while True:
        ret, frame = cam.read()
        if not ret:
            continue

        frame = cv2.resize(frame, (450, 450))
        text_ = reader.readtext(frame)

        for t_, t in enumerate(text_):
            bbox, text, score = t

            if score > threshold:
                try:
                    vehicle_exists = check(text, score)
                    color = (0, 255, 0) if vehicle_exists else (0, 0, 255)

                    cv2.putText(
                        frame, text, (int(bbox[0][0]), int(bbox[0][1])),
                        cv2.FONT_HERSHEY_COMPLEX, 0.65, color, 2)
                except Exception as e:
                    print(f"Error displaying text: {e}")

        cv2.imshow("cam", frame)

        k = cv2.waitKey(1)
        if k == ord('q'):
            print("q pressed, quitting...")
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    init_database()
    start_cam()