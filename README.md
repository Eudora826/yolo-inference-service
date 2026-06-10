# YOLO Inference Service

A containerized object detection service built with FastAPI and YOLOv8.

## Run with Docker

```bash
docker build -t yolo-inference .
docker run -d -p 8000:8000 --name yolo yolo-inference
```

## API

- `GET /health` - health check
- `POST /predict` - upload an image, returns detected objects

Example:

```bash
curl -X POST http://localhost:8000/predict -F "file=@image.jpg"
```

Interactive docs available at `http://localhost:8000/docs`.
