#!/bin/bash
# Quick script to run Question 6

echo "Building Docker image..."
docker build -t hair-classifier-lambda .

echo -e "\nStarting container..."
docker run -d -p 9000:8080 --name hair-lambda hair-classifier-lambda

echo "Waiting for container to start..."
sleep 3

echo -e "\nTesting lambda function..."
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"}'

echo -e "\n\nCleaning up..."
docker stop hair-lambda
docker rm hair-lambda

echo -e "\nDone! Check the output above for the model result."
