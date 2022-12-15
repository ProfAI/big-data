import boto3

BUCKET_NAME = "my-professionai-new-bucket"
s3 = boto3.client('s3', region_name='eu-west-1')
s3.create_bucket(Bucket=BUCKET_NAME, CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})