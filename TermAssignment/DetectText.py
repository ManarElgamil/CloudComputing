import json
import boto3

client = boto3.client('rekognition')

def lambda_handler(event, context):
    
    
    bucket = "picturesssss-bucket"
    file = event['filename']

    response = client.detect_text(Image={'S3Object': {'Bucket': bucket, 'Name': file}})
    
    output = ""
    
    for textDetection in response['TextDetections']:
        output += json.dumps(textDetection, indent=2)

    if output == "":
        return "No Text found!"
    else:
        
        return output
