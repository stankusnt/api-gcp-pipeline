import pandas as pd
import logging





def parse_api_call(data_input):
    response = {}
    def parse_json(data_input, nested_prefix: str=None, nested: bool=False) -> dict:
        # Handle lists
        if isinstance(data_input, list):
            for item in data_input:
                if isinstance(item, dict):
                    parse_json(item, nested_prefix=str('_list'))
                elif isinstance(item, str):
                    logging.warning("Error: item is a string")
        # Handle dictionaries
        elif isinstance(data_input, dict):
            for key, value in data_input.items():
                if isinstance(value, str):
                    nested_column = str(nested_prefix) + key
                    if nested_column in response:
                        response[nested_column].append(value)
                    elif nested:
                        response[nested_column] = [value]
                    elif key in response:
                        response[key].append(value)
                    else:
                        response[key] = [value]
                elif isinstance(value, dict):
                    parse_json(value, nested_prefix=str(key + '_'), nested=True)
                elif isinstance(value, list):
                    parse_json(value)
        elif isinstance(data_input, str):
            logging.warning("Error: Item is a string")
        else:
            exit
        return response

    def request_test(data_input: dict):
        expected_input_size = len(data_input['id'])
        mismatched_col_list = []
        for column, array in data_input.items():

            if len(array) != expected_input_size:
                mismatched_col_list.append(column)
                logging.warning(f'{column} does not equal {expected_input_size} with {len(array)}.')
        return mismatched_col_list

    def remove_mismatched_cols(data_input: dict, mismatched_col_list: list):
        for item in mismatched_col_list:
            data_input.pop(item)
            logging.warning(f'Removed {item} from return value.')
        return None

    response_body = parse_json(data_input)
    mismatched_col_list = request_test(response_body)
    remove_mismatched_cols(response_body, mismatched_col_list)
    # # Remove misshaped data
    # check = response_body.pop('amount_money_currency', 'receipt_url')
    # try:
    #     response_body.pop('cursor')
    # except KeyError:
    #     pass
    response_body = pd.DataFrame.from_dict(data = response_body)
    return response_body
