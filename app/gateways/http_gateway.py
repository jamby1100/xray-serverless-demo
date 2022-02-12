import requests, os
import urllib.request

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

class HttpGateway:
    @classmethod
    def send_get_request(cls, url, headers=None):
        
        payload = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        return {
            "code": response.status_code,   
            "reason": response.reason,
            "body": response.json()
        }