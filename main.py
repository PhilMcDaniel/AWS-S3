import file_transfer
import configs as cfg


file_name = 'requirements.txt'
bucket_name = 'phil-nas-backup-bucket'
S3_file_name = f'{file_name}-uploaded'


#not working due to what I modified in "file_transfer.py" s3.client vs s3.resource
file_transfer.upload_with_default_configuration(file_name,bucket_name,S3_file_name,1)

uploaded = upload_to_aws(file_name, bucket_name, S3_file_name)

#add functionality to loop through all files in folder