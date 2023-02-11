FROM jupyter/datascience-notebook:python-3.9.2

COPY packages/requirements_dev.txt .
RUN pip install -r requirements_dev.txt

WORKDIR /src
COPY . /src
