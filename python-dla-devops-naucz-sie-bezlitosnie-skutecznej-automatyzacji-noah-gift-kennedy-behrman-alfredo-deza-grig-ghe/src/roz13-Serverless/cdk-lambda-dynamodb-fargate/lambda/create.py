import json
import logging
import os
import time
import uuid
from datetime import datetime

import boto3
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Weryfikacja nieudana")
        raise Exception("Nie można utworzyć elementu todo.")
    
    timestamp = str(datetime.utcnow().timestamp())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'text': data['text'],
        'checked': False,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    # zapisanie elementu todo do bazy danych
    table.put_item(Item=item)

    # utworzenie odpowiedzi
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
