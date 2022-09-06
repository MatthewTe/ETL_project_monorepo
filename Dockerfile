#############################################################
# The Dockerfile for building and initalizing the REST API
#############################################################
# chmod +x start_server.sh

FROM python:3.8

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

COPY REST_API /REST_API

WORKDIR /REST_API

# Installing python packages:
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD ["./start_server.sh"]