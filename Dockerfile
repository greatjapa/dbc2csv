FROM ubuntu
WORKDIR /usr/src/app
COPY ["requirements.txt", "dbc2dbf.sh", "dbf2csv.py", "Makefile", "./"]
RUN apt-get update && \
    apt-get install --assume-yes python3 python3-pip git && \
    pip3 install setuptools pip --upgrade --force-reinstall && \
    git clone https://github.com/eaglebh/blast-dbf.git && \
    cd blast-dbf && \
    make && \
    pip3 install -r ../requirements.txt
