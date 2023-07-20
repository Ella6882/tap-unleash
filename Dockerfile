FROM python:3.8-slim-buster

RUN mkdir -p /external/tap-unleash/
COPY . /external/tap-unleash/
WORKDIR /external/tap-unleash
RUN ls /external/tap-unleash/
RUN pip install -e .

ENV api_key=$UNLEASH_API_KEY
ENV api_url=$UNLEASH_API_URL

CMD tap-unleash >> state.json