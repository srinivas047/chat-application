# Chat Application
A real-time chat application using AWS WebSocket API, Lambda, and DynamoDB.

## Features
- Real-time messaging.
- Stores messages in DynamoDB.

## Setup
1. Deploy the WebSocket API using AWS API Gateway.
2. Set up the DynamoDB table using `DynamoDB_setup.yml`.
3. Deploy the `websocket_handler.py` Lambda function.
