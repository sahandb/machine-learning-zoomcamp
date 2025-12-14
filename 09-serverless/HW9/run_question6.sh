#!/bin/bash
# Script to run Question 6

set -e

echo "Step 1: Pulling base Docker image..."
docker pull agrigorev/model-2025-hairstyle:v1

echo -e "\nStep 2: Building Docker image..."
docker build -t hair-classifier-lambda .

echo -e "\nStep 3: Running container in background..."
docker run -d -p 9000:8080 --name hair-classifier-test hair-classifier-lambda

# Wait a moment for the container to start
sleep 3

echo -e "\nStep 4: Testing with the image URL..."
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" \
  -d '{"url": "https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"}'

echo -e "\n\nStep 5: Cleaning up..."
docker stop hair-classifier-test
docker rm hair-classifier-test

echo -e "\nDone! Check the output above for the model result."

