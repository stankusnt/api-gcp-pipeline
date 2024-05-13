from src.create import create_payment
from src.extract import retrieve_payments
from src.load import load_payments, schema_manager
import logging
logging.basicConfig(filename='activity.log', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main():

    #create_payment.run()
    retrieve_payments.run()
    #schema_manager.run()
    load_payments.run()

if __name__ == '__main__':
    main()