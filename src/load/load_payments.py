import os
from dotenv import load_dotenv
load_dotenv()
from google.cloud import bigquery
from google.cloud import storage
import logging

def run():

    def upload_to_cloud_storage(
        bucket_name: str, 
        source_file_name, 
        destination_blob_name: str):

        """Uploads a file to the bucket."""

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        generation_match_precondition = 0

        blob.upload_from_filename(source_file_name, if_generation_match=generation_match_precondition)

        print(
            f"File {source_file_name} uploaded to {destination_blob_name}."
        )


    def upload_to_big_query(
        project_id: str,
        dataset: str, 
        source_file_name: str, 
        destination_table_name: str):

        # Construct a BigQuery client object.
        client = bigquery.Client()

        table_id = project_id + dataset + destination_table_name

        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV, skip_leading_rows=0, autodetect=True,
        )

        with open(os.environ['file_path'], "rb") as source_file:
            job = client.load_table_from_file(source_file, table_id, job_config=job_config)

        job.result()  # Waits for the job to complete.

        table = client.get_table(table_id)  # Make an API request.
        logging.info(
            "Loaded {} rows and {} columns to {}".format(
                table.num_rows, len(table.dataset), table_id
            )
        )

    def load_gcs_to_bigquery(
        project_id: str,
        dataset: str, 
        source_uri: str,
        destination_table_name: str):
        from google.cloud import bigquery

        # Construct a BigQuery client object.
        client = bigquery.Client()

        # TODO(developer): Set table_id to the ID of the table to create.
        table_id = f"{project_id}.{dataset}.{destination_table_name}"

        job_config = bigquery.LoadJobConfig(
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
        ], 
            skip_leading_rows=1,
            # The source format defaults to CSV, so the line below is optional.
            source_format=bigquery.SourceFormat.CSV,
        )

        load_job = client.load_table_from_uri(
            source_uri, table_id, job_config=job_config
        )  # Make an API request.

        load_job.result()  # Waits for the job to complete.

        destination_table = client.get_table(table_id)  # Make an API request.
        logging.info("Loaded {} rows.".format(destination_table.num_rows))

    upload_to_cloud_storage(bucket_name='data-project011997', source_file_name=os.environ['file_path'], destination_blob_name='square_payments')
    load_gcs_to_bigquery(project_id='data-engineering-423117', dataset='square', source_uri='gs://data-project011997/square_payments', destination_table_name='payments')