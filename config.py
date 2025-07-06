import os

S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME", "expense-tracker-miniproject")
CLOUDWATCH_LOG_GROUP_NAME = os.environ.get("CLOUDWATCH_LOG_GROUP_NAME", "expense-tracker-logs")

if not S3_BUCKET_NAME:
    raise ValueError("S3_BUCKET_NAME environment variable not set.")

if not CLOUDWATCH_LOG_GROUP_NAME:
    raise ValueError("CLOUDWATCH_LOG_GROUP_NAME environment variable not set.")