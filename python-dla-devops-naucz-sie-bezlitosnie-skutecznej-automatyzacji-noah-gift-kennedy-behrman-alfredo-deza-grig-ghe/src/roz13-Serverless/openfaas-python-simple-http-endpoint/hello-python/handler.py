import json
import datetime

def handle(req):
    """obsługa żądania do funkcji
    Args:
        req (str): treść żądania
    """

    current_time = datetime.datetime.now().time()
    body = {
        "message": "Otrzymano {} o {}".format(req, str(current_time))
    }

    response = {
        "statusCode": 200,
        "body": body
    }
    return json.dumps(response, indent=4)
