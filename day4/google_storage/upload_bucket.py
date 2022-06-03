import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  r'ServiceKey_GoogleCloud.json'

storage_client = storage.Client()


def upload_to_bucket(blob_name, file_path, bucket_name):
    '''
    Upload file to a bucket
    : blob_name  (str) - object name
    : file_path (str)
    : bucket_name (str)
    '''
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_path)
    return blob

upload_to_bucket(<new_name>, <current_file_path>, <bucket_name>)
