# Pull base image
#FROM python:3.7-slim
FROM python:3.7

# Set environment variables
# -----------------------------------------
# Python won't write to *.pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Console output not buffered by docker
ENV PYTHONUNBUFFERED 1

# Set work directory (where docker will execute commands from by default)
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Build cython
COPY . /code/
RUN python ./setup.py build_ext --inplace
RUN rm ./static_root/* && python ./manage.py collectstatic --noinput
#RUN apt-get update \
#    && apt-get install -y --no-install-recommends gcc \
#    && apt-get install -y build-essential \
#    && rm -rf /var/lib/apt/lists/* \
#    && python ./setup.py build_ext --inplace \
#    && apt-get purge -y --auto-remove gcc \
#    && apt-get purge -y --auto-remove build-essential

# =======================================================================================
# Working approach:
# =======================================================================================
# Pull base image
# FROM python:3.7

# Set environment variables
# -----------------------------------------
# Python won't write to *.pyc files
# ENV PYTHONDONTWRITEBYTECODE 1
# Console output not buffered by docker
# ENV PYTHONUNBUFFERED 1

# Set work directory (where docker will execute commands from by default)
# WORKDIR /code

# Install dependencies
# COPY Pipfile Pipfile.lock /code/
# RUN pip install pipenv && pipenv install --system

# Build cython
# COPY . /code/
# RUN python ./setup.py build_ext --inplace

# =======================================================================================
# First container in a two container approach (to build cython) 
# =======================================================================================
#FROM python:3.7 as builder

#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

#WORKDIR /code

#RUN pip install cython

#COPY . /code/
#RUN python ./setup.py build_ext --inplace

# =======================================================================================
# Second container in a two container approach (to run website) 
# =======================================================================================
#FROM python:3.7-slim

# Set environment variables
# -----------------------------------------
# Python won't write to *.pyc files
#ENV PYTHONDONTWRITEBYTECODE 1
# Console output not buffered by docker
#ENV PYTHONUNBUFFERED 1

# Install dependencies
#COPY Pipfile Pipfile.lock /code/
#RUN pip install pipenv && pipenv install --system
