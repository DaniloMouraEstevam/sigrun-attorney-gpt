from decouple import config
from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    account_name = config('AZURE_STORAGE_NAME')
    account_key = config('AZURE_STORAGE_KEY')
    azure_container = 'media'
    expiration_secs = None
    overwrite_files = True


class AzureStaticStorage(AzureStorage):
    account_name = config('AZURE_STORAGE_NAME')
    account_key = config('AZURE_STORAGE_KEY')
    azure_container = 'static'
    expiration_secs = None


class AzureDocumentStorage(AzureStorage):
    account_name = config('AZURE_DATA_NAME')
    account_key = config('AZURE_DATA_KEY')
    azure_container = 'document'
    expiration_secs = None
    overwrite_files = True


class AzureImageStorage(AzureStorage):
    account_name = config('AZURE_DATA_NAME')
    account_key = config('AZURE_DATA_KEY')
    azure_container = 'image'
    expiration_secs = None
    overwrite_files = True

