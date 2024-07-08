FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

# 设置 ENTRYPOINT 和 CMD
ENTRYPOINT ["python", "onHook.py"]
CMD []
