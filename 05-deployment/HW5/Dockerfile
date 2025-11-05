FROM agrigorev/zoomcamp-model:2025

RUN pip install fastapi uvicorn requests scikit-learn

COPY app.py app.py

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
