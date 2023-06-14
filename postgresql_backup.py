import psycopg2
import subprocess
import getenvs
import s3_upload

def backitup (host="localhost",port="5432",database="postgres",user="root",password="",
             backup_filename="db.sql",backup_format="p",backup_name=""):

    # establish a connection to the database
    # conn = psycopg2.connect(
    #     host=host,
    #     port=port,
    #     database=database,
    #     user=user,
    #     password=password
    # )
    # cursor = conn.cursor()

    # perform the backup using pg_dump
    backup_filename = backup_filename
    pg_dump_cmd = f"pg_dump -F {backup_format} --verbose --dbname=" + 'postgresql://{}:{}@{}:{}/{}'.format(user, password, host, port, database) + f" --file={backup_filename} --clean --create"
    status = subprocess.run(pg_dump_cmd, shell=True)

    # close the cursor and connection
    # cursor.close()
    # conn.close()
    envs = getenvs.getenvs()
    if(status.returncode==0 and envs["s3_enabled"]=="true"):
        s3_upload.upload_file(backup_filename,envs["bucket_name"],backup_name)

    return status.returncode