FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml /usr/src/app/

RUN pip3 install poetry
RUN poetry install

COPY . /usr/src/app

CMD ["poetry", "run", "python", "src/manage.py", "runserver", "0.0.0.0:8000"]
