import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ChatMessages')

def lambda_handler(event, context):
    connection_id = event['requestContext']['connectionId']
    action = json.loads(event['body']).get('action')
    if action == "send_message":
        message = json.loads(event['body']).get('message')
        table.put_item(Item={"ConnectionId": connection_id, "Message": message})
        return {"statusCode": 200, "body": "Message sent"}
    return {"statusCode": 400, "body": "Invalid action"}
