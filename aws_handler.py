import boto3
import json
import time
from datetime import datetime

# Handle both direct execution and package imports
try:
    from config import S3_BUCKET_NAME, CLOUDWATCH_LOG_GROUP_NAME
except ImportError:
    from .config import S3_BUCKET_NAME, CLOUDWATCH_LOG_GROUP_NAME


def upload_to_s3(filename):
    s3 = boto3.client("s3", region_name='ap-south-1')  # Add region here
    try:
        s3.upload_file(filename, S3_BUCKET_NAME, filename)
        print(f"{filename} uploaded to S3 bucket {S3_BUCKET_NAME}")
        return True
    except Exception as e:
        print(f"Error uploading {filename} to S3: {e}")
        return False


def log_to_cloudwatch(message):
    cloudwatch = boto3.client("logs", region_name='ap-south-1')  # Add region here
    try:
        # Create log stream if it doesn't exist
        try:
            cloudwatch.create_log_stream(
                logGroupName=CLOUDWATCH_LOG_GROUP_NAME,
                logStreamName="expense_tracker_log_stream"
            )
        except cloudwatch.exceptions.ResourceAlreadyExistsException:
            pass  # Log stream already exists

        cloudwatch.put_log_events(
            logGroupName=CLOUDWATCH_LOG_GROUP_NAME,
            logStreamName="expense_tracker_log_stream",
            logEvents=[
                {
                    "timestamp": int(round(time.time() * 1000)),
                    "message": message,
                }
            ],
        )
        print(f"Logged to CloudWatch: {message}")
        return True
    except Exception as e:
        print(f"Error logging to CloudWatch: {e}")
        return False