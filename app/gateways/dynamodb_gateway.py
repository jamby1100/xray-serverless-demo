import boto3

class DynamodbGateway:
    @classmethod
    def create_item(cls, table_name, payload):
        client = boto3.resource('dynamodb')
        table = client.Table(table_name)

        result = table.put_item(
            Item=payload
        )

        print(result)

        return result