# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:alpine

# If you prefer miniconda:
#FROM continuumio/miniconda3
LABEL MAINTAINER="Romeel Khan"

#Set least privilege user
ENV GROUP_ID=1000 \
    USER_ID=1000

#Set container work directory
WORKDIR /app

#Copy requirements.txt as it changes the least so the build cache is not invalidated for later layers
COPY requirements.txt app/requirements.txt

RUN pip install -r app/requirements.txt
RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

#Copy the app artefacts
COPY . /app
USER www

ENTRYPOINT ["python"]
CMD ["app.py"]

# Using pipenv:
#RUN python3 -m pip install pipenv
#RUN pipenv install --ignore-pipfile
#CMD ["pipenv", "run", "python3", "-m", "k8slabs"]

# Using miniconda (make sure to replace 'myenv' w/ your environment name):
#RUN conda env create -f environment.yml
#CMD /bin/bash -c "source activate myenv && python3 -m k8slabs"
