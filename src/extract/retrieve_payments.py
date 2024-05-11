from square.http.auth.o_auth_2 import BearerAuthCredentials
from square.client import Client
import os
from dotenv import load_dotenv
from utils.utils import parse_api_call
from utils.credentials import square_access
import logging
load_dotenv()


def run():
    client = square_access()
    result = client.payments.list_payments()

    response = parse_api_call(result.body)
    logging.info(response.info)

    if result.is_success():
        logging.info('API call was successful')
    elif result.is_error():
        logging.info('API call was unsuccessful')
        logging.info(result.errors)