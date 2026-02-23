FROM python:3.15.0a6-alpine3.23
WORKDIR /app
COPY app.py requirements.txt /app
RUN apk add build-base libpq libpq-dev
RUN pip3 install -r requirements.txt
CMD flask run --host 0.0.0.0 --port 8080