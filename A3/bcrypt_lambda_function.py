
import json
import bcrypt 
import requests


def lambda_handler(event, context):
    # TODO implement
    
    action = event['action']
    value = event['value']
    
   
    if action == 'bcrypt':
        
    
        # code for hashing is retrieved from https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/
        bytes = value.encode('utf-8') 
          
        # generating the salt 
        salt = bcrypt.gensalt() 
          
        # Hashing the password 
        hash = bcrypt.hashpw(bytes, salt) 
          
    
        response = {
            "banner": "B00878259",
            "result": hash,
            "arn": "arn:aws:lambda:us-east-1:590183949889:function:bcrypt-function",
            "action": "bcrypt",
            "value": value
        }
        
        url = "http://129.173.67.234:8080/serverless/end"
        
        post_response = requests.post(url, json=response)
    
    
        return {
            "banner": "B00878259",
            "result": hash,
            "arn": "arn:aws:lambda:us-east-1:590183949889:function:bcrypt-function",
            "action": "bcrypt",
            "value": value
        }
        
    else:
        
        return


