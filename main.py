from src.create import create_payment
from src.extract import retrieve_payments
import logging
logging.basicConfig(filename='activity.log', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main():

    #create_payment.run()
    retrieve_payments.run()

if __name__ == '__main__':
    main()