import cv2
import time
from utils.utilDarknet import darknet_helper


frame = cv2.imread("teste.jpg")
detections = darknet_helper(frame, 416)
for label, confidance, bbox in detections:
    x, y, w, h = bbox
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
    cv2.putText(frame, str(label), (x-5, y-5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

frame = cv2.resize(frame, (int(450*frame.shape[1]/frame.shape[0]), 450), interpolation=cv2.INTER_AREA)
cv2.imshow("camera", frame)
cv2.waitKey(0)

