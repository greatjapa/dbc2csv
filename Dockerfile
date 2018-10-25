FROM ubuntu

RUN apt-get update && apt-get install -y python3.6 python3-pip
RUN apt-get install --assume-yes git
RUN pip3 install setuptools pip --upgrade --force-reinstall

WORKDIR /usr/src/app

RUN git clone https://github.com/eaglebh/blast-dbf.git
RUN cd blast-dbf && make

COPY requirements.txt /usr/src/app/requirements.txt
COPY dbc2dbf.sh /usr/src/app/dbc2dbf.sh
COPY dbf2csv.py /usr/src/app/dbf2csv.py
COPY Makefile /usr/src/app/Makefile

RUN pip3 install -r requirements.txt
