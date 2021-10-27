# Yolo API

### How to run?
1. Download YOLO model from [here](https://pjreddie.com/media/files/yolov3.weights) and place it in ```yolo-coco``` folder.
2. Run ```docker-compose up -d``` to serve API on ```http://localhost:4232```

### Request
```yaml
{
"image": <image file>,
}
```

### Sample Response
```yaml
{"img_info": [{"height": 427, "width": 645}], "annotations": [{"label": "person", "x": "286", "w": "83", "class_id":
"0", "score": "0.9997310042381287", "y": "178", "h": "241"}, {"label": "person", "x": "35", "w": "66", "class_id": "0",
"score": "0.9995308518409729", "y": "149", "h": "206"}, {"label": "person", "x": "556", "w": "55", "class_id": "0",
"score": "0.9992658495903015", "y": "181", "h": "167"}, {"label": "person", "x": "144", "w": "49", "class_id": "0",
"score": "0.9991637468338013", "y": "178", "h": "150"}, {"label": "person", "x": "432", "w": "54", "class_id": "0",
"score": "0.9929682612419128", "y": "178", "h": "171"}, {"label": "person", "x": "235", "w": "63", "class_id": "0",
"score": "0.99217289686203", "y": "169", "h": "145"}, {"label": "person", "x": "195", "w": "37", "class_id": "0",
"score": "0.9801965355873108", "y": "154", "h": "124"}, {"label": "person", "x": "505", "w": "50", "class_id": "0",
"score": "0.9791348576545715", "y": "171", "h": "135"}, {"label": "person", "x": "399", "w": "37", "class_id": "0",
"score": "0.9625142812728882", "y": "171", "h": "99"}, {"label": "person", "x": "2", "w": "32", "class_id": "0",
"score": "0.9511436223983765", "y": "166", "h": "117"}, {"label": "person", "x": "610", "w": "32", "class_id": "0",
"score": "0.9357197880744934", "y": "176", "h": "123"}, {"label": "person", "x": "371", "w": "27", "class_id": "0",
"score": "0.8834857940673828", "y": "166", "h": "70"}, {"label": "person", "x": "96", "w": "38", "class_id": "0",
"score": "0.861023485660553", "y": "170", "h": "106"}, {"label": "handbag", "x": "338", "w": "36", "class_id": "26",
"score": "0.7896984219551086", "y": "232", "h": "68"}, {"label": "handbag", "x": "465", "w": "37", "class_id": "26",
"score": "0.6074047684669495", "y": "205", "h": "72"}]}
```
