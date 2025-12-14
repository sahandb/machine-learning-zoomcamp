import json
import onnxruntime as ort
import numpy as np
from io import BytesIO
from urllib import request
from PIL import Image

# Load the model (already in the image)
session = ort.InferenceSession("hair_classifier_empty.onnx")
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def lambda_handler(event, context):
    url = event['url']
    
    # Download and prepare image
    img = download_image(url)
    img = prepare_image(img, (200, 200))
    
    # Preprocess
    img_array = np.array(img, dtype=np.float32)
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    img_normalized = (img_array / 255.0 - mean) / std
    img_normalized = img_normalized.transpose(2, 0, 1)
    input_data = img_normalized[np.newaxis, :, :, :].astype(np.float32)
    
    # Run inference
    outputs = session.run([output_name], {input_name: input_data})
    result = float(outputs[0][0][0])
    
    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }



