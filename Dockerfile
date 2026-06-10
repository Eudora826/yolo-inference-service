FROM python:3.11-slim

WORKDIR /app

# ultralytics / opencv 需要的系统库
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 先只拷贝 requirements,利用 Docker 层缓存
# 只要 requirements 不变,这一层就不重新装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 再拷贝代码
COPY app/ ./app/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

