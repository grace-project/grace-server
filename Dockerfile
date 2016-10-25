FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /project/
WORKDIR /project/
ADD ./project/requirements.txt /project/
RUN pip install -r requirements.txt