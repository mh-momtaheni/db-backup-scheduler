import os
from dotenv import load_dotenv

def getenvs():
    load_dotenv()
    ret_dic=dict(
        db=os.getenv('DB'),
        deploy_type=os.getenv('DEPLOY_TYPE'),
        host=os.getenv('HOST'),
        port=os.getenv('PORT'),
        username=os.getenv('USERNAME'),
        password=os.getenv('PASSWORD'),
        db_name=os.getenv('DB_NAME'),
        backup_format=os.getenv('BACKUP_FORMAT'),
        save_path=os.getenv('SAVE_PATH'),
        backup_name_prefix=os.getenv('BACKUP_NAME_PREFIX'),
        s3_enabled=os.getenv('S3_ENABLED'),
        s3_host=os.getenv('S3_HOST'),
        s3_access_key_id=os.getenv('S3_ACCESS_KEY_ID'),
        s3_secret_access_key=os.getenv('S3_SECRET_ACCESS_KEY'),
        bucket_name=os.getenv('BUCKET_NAME')
    )
    return ret_dic