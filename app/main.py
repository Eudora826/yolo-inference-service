import io
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from app.detector import Detector

app = FastAPI(title="YOLO Inference Service")

# 懒加载:启动时不加载模型,第一次请求 /predict 才加载
# 这样 /health 很快,测试时也容易 mock
_detector = None


def get_detector() -> Detector:
    global _detector
    if _detector is None:
        _detector = Detector()
    return _detector


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    detections = get_detector().predict(image)
    return {"detections": detections, "count": len(detections)}
