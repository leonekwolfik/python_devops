"""GCP HTTP Cloud Function Example."""
# -*- coding: utf-8 -*-

import json
import datetime


def endpoint(request):
    """GCP HTTP Cloud Function Example.

    Args:
        request (flask.Request)

    Returns:
        Tekst odpowiedzi lub dowolny zbiór wartości, które można przekształcić na
        obiekt Response za pomocą `make_response`
        <http://flask.pocoo.org/docs/0.12/api/#flask.Flask.make_response>.

    """
    current_time = datetime.datetime.now().time()
    body = {
        "message": "Otrzymano żądanie {} o {}".format(request.method, str(current_time))
    }

    response = {
        "statusCode": 200,
        "body": body
    }

    return json.dumps(response, indent=4)
