FROM python:3.9.2

COPY jsninjify /jsninjify

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

CMD flask run --host=0.0.0.0