import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  r'ServiceKey_GoogleCloud.json'

storage_client = storage.Client()

for bucket in storage_client.list_buckets():
    print(bucket)
