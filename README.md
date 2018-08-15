# PyniBlog

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-green.svg)](/LICENSE)

A simple POC for Blog application, build with Python3 and Django 2.1.

## Tech and Libraries

- [Python3](https://www.python.org/)
- [Django 2.1](https://www.djangoproject.com/)

## Features

As commons simple blog platform, here are the essential features:

- Multi user authorization.
- Post category and tags
- Post comments
- Admin-Page: Manage users, categories, tags, posts, comments
- Front-Page: Home, About, Archive, Categories, Tags, Post
- Responsive view for both admin & front page.

All admin page operations are base on Django Admin page.

## Requirement

There are some external libraries required for this project:

- Django CKEditor, for wysiwyg editor.
  View installation [document](https://github.com/django-ckeditor/django-ckeditor#installation).

- [Django Simple Captcha](https://django-simple-captcha.readthedocs.io/en/latest/usage.html)

## Build and Testing

### Build

  For first time, run:

  ```console
  # create all required migration
  py manage.py makemigrations

  # execute the migration script
  py manage.py migrate
  ```

### Testing

_Coming soon..._


## Local Deployment

To run as local server:

```console
py manage.py runserver
```

### Admin Page

- Default admin page url is [http://localhost:8000/admin](http://localhost:8000/admin)
  
  Default admin page account is username: `admin` and password: `admin123`

## Online Demo

_Coming soon.._

## Reference and Related Documents

_Coming soon.._

## Copyright and License

Copyright 2018 Maikel Chandika (mkdika@gmail.com). Code released under the
Apache License, Version 2.0. See [LICENSE](/LICENSE) file.
