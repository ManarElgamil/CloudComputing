
import json
import boto3

client = boto3.client('rekognition')

def lambda_handler(event, context):
    bucket = "picturesssss-bucket"
    
    file = event['filename']

    response = client.detect_labels(Image={'S3Object': {'Bucket': bucket, 'Name': file}})
    
    output = ""
    
    for label in response['Labels']:
        output += json.dumps(label, indent=2)
        
        
    if output == "":
        return "No labels found!"
    else:
        
        return output


