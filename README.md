# Django APM

An "Application Performance Monitor" (APM) designed specifically for Django to aid in tracking slow 
requests and queries that can be easily reviewed from the admin.


## Install

Download the package

```
pip install django-apm
```

and add it to your Django installed apps, *as high in the INSTALLED_APPS list as possible*.

```python
INSTALLED_APPS = [
    'apm',
    # ...
]
```

finally, add the middleware, again as high in the order as possible.

```python
MIDDLEWARE = [
]
```

## Admin / Models

- Requests: all url based requests, can be standard Django views or DRF
- Queries: all sql queries, can be tied to a request (or not in the case of a command/worker)
