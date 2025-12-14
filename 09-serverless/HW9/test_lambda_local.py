#!/usr/bin/env python3
"""
Test script for Question 6 - test the lambda function locally
This can be run inside the Docker container or locally if you have the model file
"""

import json
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Mock event for testing
event = {
    'url': 'https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg'
}

# Mock context (not used in our function)
class MockContext:
    pass

context = MockContext()

try:
    # Import and test
    from lambda_function import lambda_handler
    
    result = lambda_handler(event, context)
    print(f"Result: {result}")
    model_output = json.loads(result['body'])['result']
    print(f"\nAnswer to Question 6: Model output is {model_output}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

