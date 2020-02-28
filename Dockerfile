FROM python:3.9.0a3-buster

MAINTAINER Hubert Pałasz

RUN useradd --create-home appuser

WORKDIR /home/appuser

RUN apt-get update && \
	pip3 install virtualenv

ENV VIRTUAL_ENV=.

RUN virtualenv -p /usr/bin/python3 $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
COPY app/main.py .

RUN	apt-get install -y python3-dev default-libmysqlclient-dev libssl-dev && \ 
	pip3 install -r requirements.txt && \
	chown -R appuser:appuser . && \
	chmod 777 main.py 

USER appuser

CMD ["python3", "main.py"]