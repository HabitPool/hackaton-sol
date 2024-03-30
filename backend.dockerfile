FROM python:3.11-buster as base

RUN mkdir /code
WORKDIR /code

COPY ./requirements.txt /code/
RUN pip3 install -r requirements.txt

COPY ./ /code/

ENV PYTHONPATH "/code"

CMD ["python3", "backend/app.py"]

FROM base as dev

ENV BACKEND_CONFIG_PATH "backend/config/dev.yaml"

FROM base as stg

ENV BACKEND_CONFIG_PATH "backend/config/stg.yaml"