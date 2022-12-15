import boto3

client = boto3.client("s3")
client.upload_file("./test.txt", "profession-ai-exercise", "test.txt")