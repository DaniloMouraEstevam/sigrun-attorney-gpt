from django.conf import settings
from azure.storage.blob import BlobClient
from decouple import config
import numpy as np
import cv2

def create_blob_client(file_name, container):
    try:
        return BlobClient(
            account_url=settings.AZURE_CUSTOM_DOMAIN,
            container_name=settings.AZURE_MEDIA_CONTAINER + '/' + container,
            blob_name=file_name,
            credential=config('AZURE_STORAGE_KEY'),
        )
    except Exception as e:
        print(f"Error creating BlobClient: {e}")
        return None

def upload_file_to_blob(file, file_name, extension, container):
    try:
        file_content = file.read()
        arr = np.asarray(bytearray(file_content), dtype=np.uint8)
        cv2_image = cv2.imdecode(arr, 1)  # 'Remove alpha channel'
        resized_image = cv2.resize(cv2_image, (400, 400))
        _, buffer = cv2.imencode(extension, resized_image)
        file_io = buffer.tobytes()

        blob_client = create_blob_client(file_name=file_name, container=container)
        if blob_client is not None:
            blob_client.upload_blob(data=file_io, overwrite=True)
    except Exception as e:
        print(f"Error uploading file to blob: {e}")

def delete_blob(file_name, container):
    try:
        blob_client = create_blob_client(file_name=file_name, container=container)
        if blob_client is not None:
            blob_client.delete_blob()
            print(f"Blob {file_name} deleted successfully.")
    except Exception as e:
        print(f"Error deleting blob: {e}")
