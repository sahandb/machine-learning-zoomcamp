FROM agrigorev/model-2025-hairstyle:v1

# Install required libraries
RUN pip install --no-cache-dir \
    onnxruntime \
    pillow \
    numpy

# Copy lambda function
COPY lambda_function.py ${LAMBDA_TASK_ROOT}/

# Set the CMD to your handler
CMD [ "lambda_function.lambda_handler" ]



