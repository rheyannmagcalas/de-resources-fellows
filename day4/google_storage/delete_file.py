import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  r'ServiceKey_GoogleCloud.json'

storage_client = storage.Client()

bucket = storage_client.bucket(<bucket_name>)
blob = bucket.blob("pressure.csv")
blob.delete()