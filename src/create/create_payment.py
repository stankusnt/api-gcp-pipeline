from square.http.auth.o_auth_2 import BearerAuthCredentials
from square.client import Client
from utils.credentials import square_access
import os
from dotenv import load_dotenv
load_dotenv()

def run():
    client = square_access()
    result = client.locations.list_locations()

    for i in range(101, 10000):
        result = client.payments.create_payment(
            body = {
                "source_id": "cnon:card-nonce-ok",
                "idempotency_key": f"a2193d18-eaad-46b0-be3e-850bb642eba{i+2}",
                "amount_money": {
                "amount": i+1,
                "currency": "USD"
                }
            }
        )
        yield i

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)