# infrastructure/storage.py

import json
from datetime import datetime
import os
import boto3
from loguru import logger

class StorageManager:
    def __init__(self, s3_enabled=False, bucket_name=None):
        self.s3_enabled = s3_enabled
        self.bucket_name = bucket_name
        self.local_dir = "storage"
        os.makedirs(self.local_dir, exist_ok=True)

        if self.s3_enabled:
            self.s3 = boto3.client("s3")
            logger.info(f"S3 storage enabled for bucket: {self.bucket_name}")
        else:
            logger.info("Using local storage.")

    def save(self, data: dict, prefix: str = "snapshot"):
        timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        filename = f"{prefix}_{timestamp}.json"
        path = os.path.join(self.local_dir, filename)

        with open(path, "w") as f:
            json.dump(data, f, indent=2)

        logger.debug(f"Saved snapshot to {path}")

        if self.s3_enabled:
            self.s3.upload_file(path, self.bucket_name, filename)
            logger.info(f"Uploaded {filename} to S3 bucket {self.bucket_name}")
