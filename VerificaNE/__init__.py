import fileinput as file
import pandas as pd
import logging
import azure.functions as func



def main(req: func.HttpRequest, inputblob: func.InputStream) -> func.HttpResponse:
    result = ('False')
    logging.info('starting')
    logging.info('Python HTTP trigger function processed a request.')
    body = req.params.get('body')
    processos = inputblob

    if not body:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            body = req_body.get('body')

    if body:
        for n in processos['Processo']:
            if n in body:
                result = ('True')
                return func.HttpResponse(result)
            else:
                return func.HttpResponse(
                "Please pass a message body on the query string or in the request body",
                status_code=400
                )

    return func.HttpResponse(result)