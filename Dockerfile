FROM postgres:15 AS base

COPY mongodb-tools.deb ./
RUN apt-get install ./mongodb-tools.deb 
RUN apt-get update && apt-get -y install cron  build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev

RUN wget https://www.python.org/ftp/python/3.10.11/Python-3.10.11.tgz
RUN tar -xf Python-3.10.*.tgz
RUN cd Python-3.10.*/ && ./configure --prefix=/usr/local --enable-optimizations --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib" && make -j $(nproc) &&  make altinstall


WORKDIR /app
ADD . /app
COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab


RUN python3.10 -m pip install --upgrade pip
RUN python3.10 -m pip install python-dotenv boto3
RUN python3.10 -m pip install python-dotenv psycopg2-binary

RUN chmod +x run.sh
ENTRYPOINT ["/bin/sh","-c","/bin/bash ./run.sh && cron -f"]