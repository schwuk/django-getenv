=============
django-getenv
=============

.. image:: https://badge.fury.io/py/django-getenv.svg
    :target: https://pypi.python.org/pypi/django-getenv
    
.. image:: https://travis-ci.org/schwuk/django-getenv.png?branch=master
    :target: https://travis-ci.org/schwuk/django-getenv
        
.. image:: https://landscape.io/github/schwuk/django-getenv/master/landscape.png
    :target: https://landscape.io/github/schwuk/django-getenv/master
    :alt: Code Health

A quick'n'easy way to use environment variables in your Django (and
Python) projects.

* Free software: BSD license

Introduction
------------

If you're using
`django-dotenv <https://github.com/jacobian/django-dotenv>`__ to get the
most out of your ``.env`` file, you want to use the values there in your
`Django <https://www.djangoproject.com/>`__ project's settings.

It will convert boolean, integer and float values to their native Python
types.

There's nothing here that is Django specific, but I'm using it with
Django so that's what I've called it.

Installation
------------

::

    pip install django-getenv

Usage
-----

In your ``settings.py`` file (or equivalent), add:

::

    from getenv import env

Then to read in your environment variables, do this:

::

    SECRET_KEY = env("SECRET_KEY")

If you want to provide a default (in case the environment variable isn't
set), try:

::

    SECRET_KEY = env("SECRET_KEY", "a_secret_key")

You can also use getenv in a template:

::
    {% load getenv %}

    Current path: {% getenv "PATH" %}


For best results, mix with
`django-dotenv <https://github.com/jacobian/django-dotenv>`__ and
`dj-database-url <https://github.com/kennethreitz/dj-database-url>`__.
