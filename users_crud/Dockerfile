FROM python:3.7-stretch

WORKDIR /src

ADD . /src

RUN pip3 install -r requirements.txt

# Run command to start uWSGI
CMD [ "uwsgi", "app.ini" ]
