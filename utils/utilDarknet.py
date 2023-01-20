import cv2

def darknet_helper(img, imgSize):
    model.setInputParams(size=(imgSize, imgSize), scale=1/255, swapRB=True)
    classes, scores, boxes = model.detect(img, 0.1, 0.01)
    detections = zip(classes, scores, boxes)
    return detections

net = cv2.dnn.readNetFromDarknet(
    'yolo/custom-yolov4-tiny-detector.cfg', 'yolo/custom-yolov4-tiny-detector_last 20000.weights')
model = cv2.dnn_DetectionModel(net)
