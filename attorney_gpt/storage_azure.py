from django.conf import settings
from azure.storage.blob import BlobClient
from decouple import config
import numpy as np
import cv2


def create_blob_client(file, key, domain, container, subcontainer=''):
    try:
        container_name = container
        if subcontainer:
            container_name += '/' + subcontainer
        return BlobClient(
            account_url=domain,
            container_name=container_name,
            blob_name=file,
            credential=key,
        )
    except Exception as e:
        print(f"Error creating BlobClient: {e}")
        return None

def upload_file_to_blob(file, filename, extension, params):
    try:
        file_content = file.read()

        # Check if the file is an image
        if extension.lower() in ['.jpg', '.png', '.jpeg', '.gif', '.bmp']:
            arr = np.asarray(bytearray(file_content), dtype=np.uint8)
            cv2_image = cv2.imdecode(arr, 1)
            # resized_image = cv2.resize(cv2_image, (400, 400))
            # _, buffer = cv2.imencode(extension, resized_image)
            _, buffer = cv2.imencode(extension, cv2_image)
            file_io = buffer.tobytes()
        else:
            # If the file is not an image, use the original file content
            file_io = file_content

        blob_client = create_blob_client(**params)
        if blob_client is not None:
            blob_client.upload_blob(data=file_io, overwrite=True)
        
        return blob_client.url
    except Exception as e:
        print(f"Error uploading file to blob: {e}")


# def delete_blob(file_name, container):
#     try:
#         blob_client = create_blob_client(file_name=file_name, container=container)
#         if blob_client is not None:
#             blob_client.delete_blob()
#             print(f"Blob {file_name} deleted successfully.")
#     except Exception as e:
#         print(f"Error deleting blob: {e}")
