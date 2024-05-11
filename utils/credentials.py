from square.http.auth.o_auth_2 import BearerAuthCredentials
from square.client import Client
import os
from dotenv import load_dotenv
load_dotenv()

def square_access():
    client = Client(
        bearer_auth_credentials=BearerAuthCredentials(
            access_token=os.environ['SQUARE_ACCESS_TOKEN']
        ),
        environment='sandbox')

    return client