from dotenv import load_dotenv
from utils.utils import parse_api_call
from utils.credentials import square_access
import os
import logging
import pandas as pd
import numpy as np
load_dotenv()

def run():
    counter = 0
    response_dataframes = []
    client = square_access()
    result = client.payments.list_payments()
    initial_response = parse_api_call(result.body)
    logging.info(initial_response.info)
    if result.is_success():
        response_dataframes.append(initial_response)
        # Additional logic to loop through pages in API
        while (result.body != {}):
            loop_response = parse_api_call(result.body)
            response_dataframes.append(loop_response)
            if (result.cursor):
                result = client.payments.list_payments(
                    cursor=result.cursor
                )
                counter = counter+1
            else:
                break
        response = pd.concat(response_dataframes[:-1])
        response = response.reset_index(drop=True)
        # Loading payments
        response.to_csv(os.environ['file_path'])
        logging.info('API call was successful')
    elif result.is_error():
        logging.info('API call was unsuccessful')
        logging.info(result.errors)