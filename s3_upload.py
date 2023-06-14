import json
import logging
import os
import pathlib
import sys
import threading
from typing import Optional
import getenvs

import boto3
from boto3.s3.transfer import TransferConfig
from botocore.exceptions import ClientError

# Constant variables
KB = 1024
MB = KB * KB
GB = MB * KB

# Configure logging
logging.basicConfig(level=logging.INFO)
envs = getenvs.getenvs()
# S3 client instance
s3_client = boto3.client(
    's3',
    endpoint_url=envs["s3_host"],
    aws_access_key_id=envs["s3_access_key_id"],
    aws_secret_access_key=envs["s3_secret_access_key"]
)

class ProgressPercentage:
    def __init__(self, file_path: str):
        self._file_path = file_path
        self._size = float(os.path.getsize(file_path))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        """
        To simplify, assume this is hooked up to a single file_path

        :param bytes_amount: uploaded bytes
        """
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (self._file_path, self._seen_so_far, self._size, percentage)
            )
            sys.stdout.flush()


def upload_file(file_path: str, bucket: str, object_name: Optional[str] = None):
    """
    Upload a file to an S3 bucket

    :param file_path: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_path is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_path
    if object_name is None:
        object_name = file_path

    # Upload the file
    try:
        # Set the desired multipart threshold value (400 MB)
        config = TransferConfig(multipart_threshold=400 * MB, max_concurrency=5)
        s3_client.upload_file(
            file_path,
            bucket,
            object_name,
            ExtraArgs={'ACL': 'public-read'},
            Callback=ProgressPercentage(file_path),
            Config=config
        )
    except ClientError as e:
        logging.error(e)
        return False

    return True


# file
# object_name = sys.argv[1]
# bucketname = sys.argv[2]
# file_abs_path = sys.argv[3]

# upload_file(file_abs_path, bucketname, object_name)