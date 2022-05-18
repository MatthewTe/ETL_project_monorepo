#############################################################
# The Dockerfile for building and initalizing the REST API
#############################################################
FROM python:3.8

# Creating non-root user to run in container:
RUN groupadd -g 999 django_user \
 && useradd -r -u 999 -g django_user django_user

# Adding Permissions to the Django User:

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Copying the django site files into the container: 
COPY private_rest_api /private_rest_api
RUN chown -R django_user:django_user private_rest_api

WORKDIR /private_rest_api

# Installing python packages:
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

USER django_user
