from django.db import models
from django.contrib.auth import get_user_model


class Request(models.Model):
    user = models.ForeignKey(get_user_model())


class Query(models.Model):
    request = models.ForeignKey(null=True)
