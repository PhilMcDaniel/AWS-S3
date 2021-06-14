import file_transfer
import configs as cfg

#not working due to secrets
file_transfer.upload_with_default_configuration('requirements.txt',cfg.BUCKET_NAME,cfg.ACCESS_KEY_ID,1)