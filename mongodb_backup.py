import subprocess
import subprocess
import getenvs
import s3_upload

def backitup (host="localhost",password="",db_name="",backup_filename="dbs.bak",backup_name=""):

    backup_filename=backup_filename+'.gz'
    dump_cmd= 'mongodump --uri="'+host+'" --password '+password +' --verbose --gzip --archive='+backup_filename+' --db='+db_name
    status = subprocess.run(dump_cmd, shell=True)

    envs = getenvs.getenvs()
    if(status.returncode==0 and envs["s3_enabled"]=="true"):
        s3_upload.upload_file(backup_filename,envs["bucket_name"],backup_name)
    return status.returncode