import json
import os

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

from app.gateways.dynamodb_gateway import DynamodbGateway
from app.gateways.http_gateway import HttpGateway
from app.gateways.elasticsearch_gateway import ElasticsearchGateway

patch_all()

def hello(event, context):
    table_name = os.getenv("DYNAMODB_REQUEST_TABLE")
    beta_system_url = os.getenv("BETA_SYSTEM_URL")

    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    request_id = event['requestContext']["requestId"]
    DynamodbGateway.create_item(table_name, {"request_id": request_id, "master": 1})

    HttpGateway.send_get_request(beta_system_url)

    return response

def homepage(event, context):
    query = {
        "query": {
            "match_all": {}
        }
    }

    index_name = "product-index-variant-migrated"

    subsegment = xray_recorder.begin_subsegment('annotations')
    subsegment.put_annotation('action', 'elasticsearch')

    result = ElasticsearchGateway.search_index(index_name, query)
    xray_recorder.end_subsegment()

    body = {
        "message": "Homepage Items",
        "input": [{"name": "Vodka Premium", "price": 300}, {"name": "Cassava Prime", "price": 1000}],
        "items_searched": result
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
