import json
import hashlib
import requests


def lambda_handler(event, context):
    # TODO implement
    
    # parsed_input = json.loads(event['input'])
    
    # parsed_input = event['input']
    
    # Extract the action and value fields
    # action = parsed_input['action']
    # value = parsed_input['value']
    
    action = event['action']
    value = event['value']
    
   

    if action == 'sha256':

        # code for hashing is retrieved from https://stackoverflow.com/questions/48613002/sha-256-hashing-in-python
        hashed_value = hashlib.sha256(value.encode('utf-8')).hexdigest()
     
        response = {
            "banner": "B00878259",
            "result": hashed_value,
            "arn": "arn:aws:lambda:us-east-1:590183949889:function:sha-function",
            "action": "sha256",
            "value": value
        }
        
        url = "http://129.173.67.234:8080/serverless/end"
        
        post_response = requests.post(url, json=response)


        return {
            "banner": "B00878259",
            "result": hashed_value,
            "arn": "arn:aws:lambda:us-east-1:590183949889:function:sha-function",
            "action": "sha256",
            "value": value
        }
        
    else:
        
        return

