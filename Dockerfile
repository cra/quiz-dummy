FROM python:3.9

LABEL maintainer=shrimpsizemoose

ENV PYHTONUNBUFFERED=1

RUN pip install Django==3.1.7 gunicorn

RUN mkdir -p /code/config
COPY dummy-quizzer/config/asgi.py /code/config/
COPY dummy-quizzer/config/__init__.py /code/config/
COPY dummy-quizzer/config/settings.py /code/config/
COPY dummy-quizzer/config/urls.py /code/config/
COPY dummy-quizzer/config/views.py /code/config/
COPY dummy-quizzer/config/wsgi.py /code/config/

COPY dummy-quizzer/manage.py /code/

EXPOSE 8000

COPY ./docker-entrypoint.sh /code/
WORKDIR /code

ENTRYPOINT ["./docker-entrypoint.sh"]
