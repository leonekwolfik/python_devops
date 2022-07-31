import os

import boto3
dynamodb = boto3.resource('dynamodb')


def delete(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # usunięcie elementu todo z bazy danych
    table.delete_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # utworzenie odpowiedzi
    response = {
        "statusCode": 200
    }

    return response
