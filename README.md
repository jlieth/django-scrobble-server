[![Build Status](https://travis-ci.org/jlieth/django-scrobble-server.svg?branch=master)](https://travis-ci.org/jlieth/django-scrobble-server)
[![Coverage Status](https://coveralls.io/repos/github/jlieth/django-scrobble-server/badge.svg?branch=master)](https://coveralls.io/github/jlieth/django-scrobble-server?branch=master)
[![codecov](https://codecov.io/gh/jlieth/django-scrobble-server/branch/master/graph/badge.svg)](https://codecov.io/gh/jlieth/django-scrobble-server)

# django-scrobble-server

Django app implementing the server-side Audioscrobbler protocol

## Installation

Install via pip into a `virtualenv`:
```bash
pip install git+https://github.com/jlieth/django-scrobble-server
```

## Available components
The functionality is split into different sub-apps. Currently available apps:
- `scrobble_server.core`: Core functionality (music and submission models, chart functionality). **Required**
- `scrobble_server.api.v12`: Support for the Audioscrobbler 1.2 protocol

This allows you to choose which apps you actually want to use. There is obviously not much of a choice
right now, but I do plan to implement the Audioscrobbler/Last.fm protocol 2.0 at some point.

## Setup
In `settings.py`, add the apps you want to use:
```python
INSTALLED_APPS = (
    ...
    "scrobble_server.core",
    "scrobble_server.api.v12",
)
```

Execute migrations:
```bash
python manage.py migrate
```

Include the urls in your `urls.py`:
```python
from django.urls import include, path

urlpatterns = [
    ...
    path("url-prefix/", include("scrobble_server.urls")),
    ...
]
```
