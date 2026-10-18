FROM python:3.12-slim
WORKDIR /app
COPY pipeline.py api.py ./
COPY data/hour.csv data/hour.csv
RUN python pipeline.py
CMD ["python", "pipeline.py"]
