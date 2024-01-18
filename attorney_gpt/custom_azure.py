from decouple import config
from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    account_name = config('AZURE_ACCOUNT_NAME')
    account_key = config('AZURE_STORAGE_KEY')
    azure_container = 'media'
    expiration_secs = None
    overwrite_files = True


class AzureStaticStorage(AzureStorage):
    account_name = config('AZURE_ACCOUNT_NAME')
    account_key = config('AZURE_STORAGE_KEY')
    azure_container = 'static'
    expiration_secs = None