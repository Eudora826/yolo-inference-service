from ultralytics import YOLO
from PIL import Image


class Detector:
    def __init__(self, model_path: str = "yolov8n.pt"):
        # yolov8n 是最小的模型,首次运行会自动下载权重
        self.model = YOLO(model_path)

    def predict(self, image: Image.Image):
        results = self.model(image)
        detections = []
        for r in results:
            for box in r.boxes:
                detections.append({
                    "class": self.model.names[int(box.cls)],
                    "confidence": round(float(box.conf), 4),
                    "bbox": [round(float(x), 2) for x in box.xyxy[0]],
                })
        return detections
