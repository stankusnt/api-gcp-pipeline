import os
from dotenv import load_dotenv
load_dotenv()
from google.cloud import bigquery
from google.cloud import storage

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
        project_name: str,
        schema: str, 
        source_file_name: str, 
        destination_table_name: str):

        # Construct a BigQuery client object.
        client = bigquery.Client()

        table_id = project_name + schema + destination_table_name

        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV, skip_leading_rows=0, autodetect=True,
        )

        with open(os.environ['file_path'], "rb") as source_file:
            job = client.load_table_from_file(source_file, table_id, job_config=job_config)

        job.result()  # Waits for the job to complete.

        table = client.get_table(table_id)  # Make an API request.
        print(
            "Loaded {} rows and {} columns to {}".format(
                table.num_rows, len(table.schema), table_id
            )
        )

    upload_to_cloud_storage(bucket_name='data-project011997', source_file_name=os.environ['file_path'], destination_blob_name='square_payments')