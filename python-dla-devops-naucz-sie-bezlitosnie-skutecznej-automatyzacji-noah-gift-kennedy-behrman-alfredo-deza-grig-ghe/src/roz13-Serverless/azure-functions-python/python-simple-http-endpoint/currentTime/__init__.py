import logging

import azure.functions as func
import datetime


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Funkcja Pythona wyzwalania HTTP przetworzyła żądanie.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    current_time = datetime.datetime.now().time()
    if name:
        return func.HttpResponse(f"Witaj, {name}, teraz jest godzina {current_time}!")
    else:
        return func.HttpResponse(
             "Proszę podać imię w ciągu kwerendy lub w treści żądania",
             status_code=400
        )
