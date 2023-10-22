# Specify the source directory
SOURCE_DIR="./src/data/clinical-trials/drive-download-20231012T194543Z-001"

# Specify the S3 bucket name
BUCKET_NAME="dte-clinical-trials"

# Upload CSV files to S3
aws s3 cp $SOURCE_DIR s3://$BUCKET_NAME/ --recursive --exclude "*" --include "*.csv"