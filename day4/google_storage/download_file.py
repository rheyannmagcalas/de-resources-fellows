import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  r'ServiceKey_GoogleCloud.json'

storage_client = storage.Client()

bucket = storage_client.get_bucket(<bucket_name>)
blob = bucket.blob("pressure.csv")
# Download the file to a destination
blob.download_to_filename('test.csv')