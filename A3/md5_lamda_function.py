
import hashlib
import json
import requests

def lambda_handler(event, context):
  

    action = event['action']
    value = event['value']
    
   
    

    if action == 'md5':
    
        # code for hashing is retrieved from https://www.geeksforgeeks.org/md5-hash-python/
        hashed_value = hashlib.md5(value.encode('utf-8')).hexdigest()
    
        response = {
            "banner": "B00878259",
            "result": hashed_value,
            # change this arn once you create it, or actually just create it
            "arn": "arn:aws:lambda:us-east-1:590183949889:function:md5",
            "action": "md5",
            "value": value
        }
        
        url = "http://129.173.67.234:8080/serverless/end"
        
        post_response = requests.post(url, json=response)
    
    
        return {
            "banner": "B00878259",
            "result": hashed_value,
            "arn": "arn:aws:lambda:us-east-1:590183949889:function:md5",
            "action": "md5",
            "value": value
        }
        
    else:
        
        return

