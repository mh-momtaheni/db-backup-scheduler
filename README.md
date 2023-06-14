
# Database Backup Utility

A production ready database backup utility which schedule, run and upload your necessary databases include PostgreSql and MongoDB

## Key features:
* Run db backups immediatly after running 
* Crontab compatible for schedule backups
* Environment(.env) dependent

## Setup
* Run docker build to create docker image of the project
```Docker
docker build -t backup-utility .
```
* Define a `.env` file at the root of the project. 

| Key  | Description |
| ------------- | ------------- |
| DB  | DB Engine: postgresql/mongodb  |
| HOST  | Db Hostname/Ip  |
| PORT | Db hosted port if needed |
| USERNAME | Db authentication username |
| PASSWORD | Db authentication password |
| DB_NAME | Database name to backup |
| BACKUP_FORMAT | postgresql backup format (p,c,d,t) |
| SAVE_PATH | Set this option when need to mount a volume to backup storage |
| BACKUP_NAME_PREFIX | A prefix for backups name |
| S3_ENABLED | true, false |
| S3_HOST | AWS S3 host |
| S3_ACCESS_KEY_ID | AWS S3 access key |
| S3_SECRET_ACCESS_KEY | AWS S3 secret key |
| BUCKET_NAME | AWS S3 bucket name |
| CRON_SCHEDULE | Crontab compatible schedule (* * * * *) |

* Run docker build to create docker image of the project
```Docker
docker run -d --name backup-utility --env-file .env backup-utility
docker logs backup-utility
```