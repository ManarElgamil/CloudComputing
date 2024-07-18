iimport json
import boto3

client = boto3.client('rekognition')

def lambda_handler(event, context):
    
    bucket = "picturesssss-bucket"
    file = event['filename']

    response = client.detect_faces(Image={'S3Object': {'Bucket': bucket, 'Name': file}}, Attributes=['ALL'])
    
    output = ""
    
    for face in response['FaceDetails']:
        output += json.dumps(face, indent=2)
        
    if output == "":
        return "No Faces found!"
    else:
        
        return output
        
