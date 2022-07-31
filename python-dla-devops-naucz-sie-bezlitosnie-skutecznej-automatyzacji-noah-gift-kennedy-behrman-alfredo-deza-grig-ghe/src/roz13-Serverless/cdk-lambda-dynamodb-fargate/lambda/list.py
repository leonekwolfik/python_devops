import json
import os

import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def list(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # pobranie wszystkich elementów todo z bazy danych
    result = table.scan()

    # utworzenie odpowiedzi
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }

    return response
