import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  r'ServiceKey_GoogleCloud.json'

storage_client = storage.Client()


bucket = storage_client.bucket(<bucket_name>)
bucket.storage_class = 'STANDARD' # Archive | Nearline | Standard | Coldline
bucket.location = 'asia-southeast1'   # https://cloud.google.com/storage/docs/locations
bucket = storage_client.create_bucket(bucket)
