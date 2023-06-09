import os

from azure.storage.blob import BlobServiceClient
from azure.storage.blob import ContainerClient
from dotenv import load_dotenv

load_dotenv()

sas_secret = os.getenv("SAS_TOKEN")
storage_account = os.getenv("STORAGE_ACCOUNT")
container_raw = os.getenv("CONTAINER_RAW")


def download_blob_to_string(
    blob_service_client: BlobServiceClient, container_name, file_name
):
    blob_client = blob_service_client.get_blob_client(
        container=container_name, blob=file_name
    )

    # encoding param is necessary for readall() to return str, otherwise it returns bytes
    downloader = blob_client.download_blob(max_concurrency=1, encoding="UTF-8")
    blob_text = downloader.readall()
    print(f"{blob_text}")


service = BlobServiceClient(
    account_url=f"https://{storage_account}.blob.core.windows.net/",
    credential=sas_secret,
)


container = ContainerClient.from_connection_string(
    conn_str=f"BlobEndpoint=https://{storage_account}.blob.core.windows.net/;SharedAccessSignature={sas_secret}",
    container_name=container_raw,
)

# YUCK! - why leaving the commented out code in?
# blob_list = container.list_blobs()
# for blob in blob_list:
#    print(f"Blob name: {blob.name}")
#    download_blob_to_string(service, container_raw, blob.name)


download_blob_to_string(
    blob_service_client=service,
    container_name=container_raw,
    file_name="art/art_stuff.csv",
)
