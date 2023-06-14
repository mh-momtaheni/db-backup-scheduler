import asyncio
import getenvs
import postgresql_backup
import mongodb_backup
import datetime
import sys


def main():
    envs=getenvs.getenvs()
    now_formatted=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_name=envs["backup_name_prefix"]+"-"+now_formatted
    filename=envs["save_path"]+backup_name+".bak"
    
    if envs["db"]=="postgresql":
        result=postgresql_backup.backitup(
            host=envs["host"],
            port=envs["port"],
            database=envs["db_name"],
            user=envs["username"],
            password=envs["password"],
            backup_filename=filename,
            backup_format=envs["backup_format"],
            backup_name=backup_name
            )
        if result==0:
            sys.stdout.write("Database "+envs["db_name"]+" Backup taken and saved: "+filename)
            sys.stdout.flush()
    elif envs["db"]=="mongodb":
        result=mongodb_backup.backitup(
            host=envs["host"],
            password=envs["password"],
            db_name=envs["db_name"],
            backup_filename=filename,
            backup_name=backup_name
        )
        if result==0:
            sys.stdout.write("Database mongo Backup taken and saved: "+filename)
            sys.stdout.flush()

if __name__ == "__main__":
    main()
