# Dockerfile
FROM python:3.9.10-alpine3.14
WORKDIR /srv
RUN pip install --upgrade pip
RUN pip install flask pymongo
COPY . /srv
CMD ["python","process.py"]
