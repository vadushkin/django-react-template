# Backend on Django Rest Framework


Installation
------------

Create file `.env` or delete `.example` in the `.env.example` file

Fill in the data in the file `.env`

```dotenv
SECRET_KEY=KEY
DEBUG='1 - True, 0 - False'
ALLOWED_HOSTS=localhost,127.0.0.1,etc...
```

### Install requirements
```
poetry install
```

Run
---

### Migrate migrations
```
poetry run python manage.py migrate
```

### Create a superuser
```
poetry run python manage.py createsuperuser
```

### Run the server
```
poetry run python manage.py runserver
```
