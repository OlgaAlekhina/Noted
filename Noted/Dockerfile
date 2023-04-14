FROM python:3.9.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./Noted .
RUN set -ex &&\
    python3 -m pip install --no-cache-dir --no-warn-script-location --upgrade pip &&\
    python3 -m pip install --no-cache-dir --no-warn-script-location --user -r requirements.txt

#ENTRYPOINT [ "python3", "-m", "gunicorn", "-b", "0.0.0.0:80", "Noted.wsgi", "--reload" ]
ENTRYPOINT [ "python3", "manage.py", "runserver", "0.0.0.0:8080" ]
