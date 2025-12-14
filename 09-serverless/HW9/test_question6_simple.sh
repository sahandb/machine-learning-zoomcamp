#!/bin/bash
# Simple test for Question 6 - runs the test script inside the container

set -e

echo "Building Docker image..."
docker build -t hair-classifier-lambda .

echo -e "\nRunning test inside container..."
docker run --rm \
  -v "$(pwd)/test_lambda_local.py:/var/task/test_lambda_local.py" \
  hair-classifier-lambda \
  python test_lambda_local.py

