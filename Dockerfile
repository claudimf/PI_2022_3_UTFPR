FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /server
ADD requirements.txt /server
RUN pip install --upgrade pip
RUN pip install -r requirements.txt