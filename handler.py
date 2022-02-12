import json
import os

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

from app.gateways.dynamodb_gateway import DynamodbGateway

patch_all()

def hello(event, context):
    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    request_id = event['requestContext']["requestId"]
    table_name = os.getenv("DYNAMODB_REQUEST_TABLE")
    DynamodbGateway.create_item(table_name, {"request_id": "request_id", "master": 1})

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
