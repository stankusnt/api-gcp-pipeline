import logging
from google.cloud import bigquery

def run():
    client = bigquery.Client()
    def create_bq_dataset(
        dataset: str):


        dataset_id = "{}."f"{dataset}".format(client.project)

        # Construct a full Dataset object to send to the API.
        dataset = bigquery.Dataset(dataset_id)

        # TODO(developer): Specify the geographic location where the dataset should reside.
        dataset.location = "US"

        dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.
        logging.info("Created dataset {}.{}".format(client.project, dataset.dataset_id))

    def create_bq_table(
        project_id: str,
        dataset: str, 
        destination_table_name: str):

        # TODO(developer): Set table_id to the ID of the table to create.
        table_id = f"{project_id}.{dataset}.{destination_table_name}"

        schema = [
            bigquery.SchemaField("index", "NUMERIC"),
            bigquery.SchemaField("id", "STRING"),
            bigquery.SchemaField("created_at", "STRING"),
            bigquery.SchemaField("updated_at", "STRING"),
            bigquery.SchemaField("status", "STRING"), 
            bigquery.SchemaField("delay_duration", "STRING"),
            bigquery.SchemaField("source_type", "STRING"),
            bigquery.SchemaField("card_details_status", "STRING"),
            bigquery.SchemaField("card_card_brand", "STRING"),
            bigquery.SchemaField("card_last_4", "STRING"),
            bigquery.SchemaField("card_exp_month", "INT64"),
            bigquery.SchemaField("card_exp_year", "INT64"),
            bigquery.SchemaField("card_fingerprint", "STRING"),
            bigquery.SchemaField("card_card_type", "STRING"),
            bigquery.SchemaField("card_prepaid_type", "STRING"),
            bigquery.SchemaField("card_bin", "INT64"),
            bigquery.SchemaField("card_details_entry_method", "STRING"),
            bigquery.SchemaField("card_details_cvv_status", "STRING"),
            bigquery.SchemaField("card_details_avs_status", "STRING"),
            bigquery.SchemaField("card_details_statement_description", "STRING"),
            bigquery.SchemaField("card_payment_timeline_authorized_at", "STRING"),
            bigquery.SchemaField("card_payment_timeline_captured_at", "STRING"),
            bigquery.SchemaField("location_id", "STRING"),
            bigquery.SchemaField("order_id", "STRING"),
            bigquery.SchemaField("risk_evaluation_created_at", "STRING"),
            bigquery.SchemaField("risk_evaluation_risk_level", "STRING"),
            bigquery.SchemaField("effective_at", "STRING"),
            bigquery.SchemaField("type", "STRING"),
            bigquery.SchemaField("total_money_amount", "INT64"),
            bigquery.SchemaField("total_money_currency", "STRING"),
            bigquery.SchemaField("approved_money_amount", "INT64"),
            bigquery.SchemaField("approved_money_currency", "STRING"),
            bigquery.SchemaField("receipt_number", "STRING"),
            bigquery.SchemaField("receipt_url", "STRING"),
            bigquery.SchemaField("delay_action", "STRING"),
            bigquery.SchemaField("delayed_until", "STRING"),
            bigquery.SchemaField("application_details_square_product", "STRING"),
            bigquery.SchemaField("application_details_application_id", "STRING"),
            bigquery.SchemaField("version_token", "STRING")
        ]

        table = bigquery.Table(table_id, schema=schema)
        table = client.create_table(table)  # Make an API request.
        logging.info(
            "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
        )

    #create_bq_dataset(dataset='square')
    create_bq_table(project_id='data-engineering-423117', dataset='square', destination_table_name='payments')
    