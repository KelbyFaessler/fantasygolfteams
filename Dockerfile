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
#COPY setup.py /code/
COPY ./bbmajors_compute/compute_engine/engine/ /code/bbmajors_compute/compute_engine/engine/
COPY . /code/
RUN python ./printpaths.py
RUN python ./setup.py build_ext --inplace
#RUN apt-get update \
#    && apt-get install -y --no-install-recommends gcc \
#    && apt-get install -y build-essential \
#    && rm -rf /var/lib/apt/lists/* \
#    && python ./setup.py build_ext --inplace \
#    && apt-get purge -y --auto-remove gcc \
#    && apt-get purge -y --auto-remove build-essential

# Copy project
#COPY . /code/
#RUN cp -a /code/engine/. /code/bbmajors_compute/compute_engine/engine/
#RUN rm -rf /code/engine/
RUN ls -la /code/
RUN ls -la /code/bbmajors_compute
RUN ls -la /code/bbmajors_compute/compute_engine
RUN ls -la /code/bbmajors_compute/compute_engine/engine/