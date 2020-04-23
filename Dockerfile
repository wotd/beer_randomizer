FROM python:3.6-slim-buster

WORKDIR /beer_randomizer

RUN pip install \
    dataclasses

COPY beer.py /beer_randomizer

CMD [ "python3", "/beer_randomizer/beer.py" ]