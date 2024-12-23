import cv2
import torch
import easyocr
import yolov5

model = yolov5.load('keremberke/yolov5m-license-plate')
cap = cv2.VideoCapture(0)  # Default camera
authorized_plates = ["SZ2813", "LICENSE", "LICENSE"]
reader = easyocr.Reader(['en'])
confidence_threshold = 0.5

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

            cv2.rectangle(frame, (x1_orig, y1_orig), (x2_orig, y2_orig), (0, 255, 0), 2)
            license_plate = frame[y1_orig:y2_orig, x1_orig:x2_orig]
            result = reader.readtext(license_plate, paragraph=False)
            license_plate_text = ''.join([line[1].upper().replace(" ", "") for line in result])

            is_authorized = any(
                sum(1 for char in authorized_plate if char in license_plate_text) >= 4 
                for authorized_plate in authorized_plates
            )

            gate_status = "Authorized" if is_authorized else "Guest Car"
            color = (0, 255, 0) if is_authorized else (0, 0, 255)

            cv2.putText(frame, license_plate_text, (x1_orig, y1_orig - 10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            cv2.putText(frame, gate_status, (x1_orig, y1_orig - 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    cv2.imshow("License Plate Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()