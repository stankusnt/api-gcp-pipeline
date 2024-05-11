from square.http.auth.o_auth_2 import BearerAuthCredentials
from square.client import Client
import os
from dotenv import load_dotenv
load_dotenv()

def run():

    client = Client(
        bearer_auth_credentials=BearerAuthCredentials(
            access_token=os.environ['SQUARE_ACCESS_TOKEN']
        ),
        environment='sandbox')

    result = client.locations.list_locations()

    for i in range(101, 100000):
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

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)