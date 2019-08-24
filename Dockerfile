FROM python:3.7-alpine

ARG PORT=8050
ENV PORT=${PORT}

LABEL version="0.1" description="Gloomhaven Campaign Manager" maintainer="chris@cjadkins.com"

RUN mkdir -p /app
COPY requirements.txt /app
WORKDIR /app

RUN apk add --no-cache --virtual .build-deps \
  gcc \
  libc-dev \
  && pip3 install --no-cache-dir -r requirements.txt \
  && pip3 install --no-cache-dir gunicorn \
  && apk del .build-deps

COPY . .

EXPOSE ${PORT}

CMD gunicorn -w 2 --bind :${PORT} gloomhaven:app.server