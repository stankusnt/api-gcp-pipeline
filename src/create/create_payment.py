from utils.credentials import square_access
from dotenv import load_dotenv
import logging
load_dotenv()

def run():
    client = square_access()

    for i in range(300, 500):
        result = client.payments.create_payment(
            body = {
                "source_id": "cnon:card-nonce-ok",
                "idempotency_key": f"a2193d18-eaad-46b0-be3e-850bb642eba{i+1}",
                "amount_money": {
                "amount": i+1,
                "currency": "USD"
                }
            }
        )
        print(i)
        if result.is_success():
            logging.info("Successfully created payment.")
        elif result.is_error():
            logging.info('Unsuccessful in creating payments.')
            logging.error(result.errors)