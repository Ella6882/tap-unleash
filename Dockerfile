FROM python:3.8-slim-buster

ARG api_key=default_value
ARG api_url=default_value
ENV api_key=$api_key
ENV api_url=$api_url

RUN mkdir -p /external/tap-unleash/
COPY . /external/tap-unleash/
WORKDIR /external/tap-unleash
RUN pip install -e .

CMD tap-unleash --config /external/tap-unleash/.secrets/client_secrets.json >> state.json