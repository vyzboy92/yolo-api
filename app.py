from flask import Flask, request
import numpy as np
import cv2
import os
import json

app = Flask(__name__)

labelsPath = os.path.sep.join(["yolo-coco", "coco.names"])
LABELS = open(labelsPath).read().strip().split("\n")

weightsPath = os.path.sep.join(["yolo-coco", "yolov3.weights"])
configPath = os.path.sep.join(["yolo-coco", "yolov3.cfg"])

net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

@app.route('/object_detect', methods=['POST'])
def object_detect():
    boxes = []
    confidences = []
    classIDs = []
    conf = 0.5
    thresh = 0.3
    b_box = dict()
    annotation_list = []
    resp = dict()
    img_info = dict()

    image = request.files['image'].read()
    image = np.fromstring(image, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    (H, W) = image.shape[:2]

    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
	swapRB=True, crop=False)
    net.setInput(blob)
    layerOutputs = net.forward(ln)

    for output in layerOutputs:
        
        for detection in output:
            
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            if confidence > conf:
                
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")

                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, conf, thresh)

    
    if len(idxs) > 0:
        
        for i in idxs.flatten():

            b_box['class_id'] = str(classIDs[i])
            b_box['label'] = LABELS[classIDs[i]]
            b_box['x'] = str(boxes[i][0])
            b_box['y'] = str(boxes[i][1])
            b_box['w'] = str(boxes[i][2])
            b_box['h'] = str(boxes[i][3])
            b_box['score'] = str(confidences[i])
            annotation_list.append(b_box.copy())

    img_info['width'] = W
    img_info['height'] = H
    resp['img_info'] = [img_info]
    resp['annotations'] = annotation_list

    return json.dumps(resp)
app.run(host='0.0.0.0', port=4232, debug=True, use_reloader=False)
