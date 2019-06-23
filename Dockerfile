FROM python:3.7.3-stretch
RUN pip install pipenv
RUN echo "#settings:\n #cloud: \n #token:" > /.bzt-rc
WORKDIR /app
COPY . /app/

