# PyniBlog

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-green.svg)](/LICENSE)
[![Build Status](https://travis-ci.org/mkdika/pyniblog.svg?branch=master)](https://travis-ci.org/mkdika/pyniblog)
[![codecov](https://codecov.io/gh/mkdika/pyniblog/branch/master/graph/badge.svg)](https://codecov.io/gh/mkdika/pyniblog)
[![codebeat badge](https://codebeat.co/badges/9298084a-61f8-4789-9d87-a0ec77a07655)](https://codebeat.co/projects/github-com-mkdika-pyniblog-master)



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

- [Python 3.6.x](https://www.python.org/downloads/) or more updated.

- [Django 2.x](https://docs.djangoproject.com/en/2.1/topics/install/), 
  I used Django 2.1 when this project was built.

- [Django CKEditor](https://github.com/django-ckeditor/django-ckeditor#installation), for wysiwyg editor.

- [Django Simple Captcha](https://django-simple-captcha.readthedocs.io/en/latest/usage.html)

### Test Framework and Libraries

- [Unittests](https://docs.python.org/3/library/unittest.html), unit test framework.

- [PyHamcrest](https://github.com/hamcrest/PyHamcrest), objects matcher test lib.

- [Unittests.Mock](https://docs.python.org/3/library/unittest.mock.html), mock test lib.

- [Coverage](https://coverage.readthedocs.io/en/coverage-4.5.1a/), coverage unit test lib.

Or view the `requirements.txt` file.

## Build and Testing

### Install Dependencies from requirement.txt

From projecr root, run:

```console
pip install -r requirements.txt
```

### Build

- Blog Setup

  For blog setup please open and edit the `blog/blogsettings.py` with your own preference.

- For first time, run:

  ```console
  # create all required migration
  py manage.py makemigrations

  # execute the migration script
  py manage.py migrate
  ```

### Testing

```console
# run the Django unit test
py manage.py test

# run the coverage unit test
coverage run --source='.' manage.py test blog

# view terminal coverage report
coverage report

# view html coverage report
coverage html

# erase/remove gathered data
coverage erase
```


## Local Deployment

To run as local server:

```console
py manage.py runserver
```

### Main Page

Main page (front-page) can be access from [http://localhost:8000](http://localhost:8000)

### Admin Page

- Default admin page url is [http://localhost:8000/admin](http://localhost:8000/admin)
  
  Default admin page account is username: `admin` and password: `admin123`

## Online Demo

_Coming soon.._

## Related Documents

- [Django - Writing and Running Test](https://docs.djangoproject.com/en/2.1/topics/testing/overview/)
- [Codecov Python Example](https://github.com/codecov/example-python)
- [Set Up Travis CI For Django project](https://medium.com/@MicroPyramid/set-up-travis-ci-for-django-project-427d6dd2f46c)

## Copyright and License

Copyright 2018 Maikel Chandika (mkdika@gmail.com). Code released under the
Apache License, Version 2.0. See [LICENSE](/LICENSE) file.
