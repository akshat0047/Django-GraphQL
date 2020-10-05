# GraphQL-Blog
A backend API on Django with some basic operations using GraphQL.

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

## Tech Stack
- Python
- Django
- GraphQL
- Graphene

## Requirements
- Python 3
- pip

## Getting Started

- Create a virtual environment

```
$ python -m venv venv
```

- Install Requirements

```
$ pip install -r requirements/local.txt
```

- Rename and modify .env file

```
$ cd Blog/Blog/settings
$ cp .env.example .env
```

- Create Migrations for our app

```
$ python manage.py makemigrations reckonsys
```

- Create the database

```
$ python manage.py migrate
```

- Start Django server

```
$ python manage.py runserver
```

- Visit the url in a web-browser

---

## Deployment

The repository has a GitHub hook setup on the master branch which deloys the API on heroku, here.

![deploy-to-heroku](https://www.herokucdn.com/deploy/button.svg)
