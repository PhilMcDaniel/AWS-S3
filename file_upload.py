import boto3
from botocore.exceptions import NoCredentialsError
import configs

ACCESS_KEY = configs.AccessKeyId
SECRET_KEY = configs.SecretKey

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

file = 'requirements.txt'
bucket = 'phil-nas-backup-bucket'
s3file = 'asdfasdf.txt'

uploaded = upload_to_aws(file, bucket, s3file)