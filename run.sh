#! /bin/sh
CRON_SCHEDULE=`sed -e 's/^"//' -e 's/"$//' <<<"$CRON_SCHEDULE"`
sed -i "s/#__placeholder__/$CRON_SCHEDULE/g" /etc/cron.d/crontab
/usr/bin/crontab /etc/cron.d/crontab
/bin/sh -c printenv > /app/.env