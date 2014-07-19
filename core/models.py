from datetime import datetime
from django.db import models
from random import getrandbits


def code_generator():
    return "%0x" % getrandbits(64)


class Developer(models.Model):
    created_at = models.DateTimeField(default=datetime.now, editable=False)
    username = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=32, default=code_generator, editable=False)

    def __unicode__(self):
        return "{0} ({1})".format(self.username, self.code)


class User(models.Model):
    created_at = models.DateTimeField(default=datetime.now, editable=False)
    created_by = models.ForeignKey(Developer, editable=False)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    avatar_url = models.URLField(max_length=255, blank=True)
    password = models.CharField(max_length=255)

    def __unicode__(self):
        return "{0} {1} aka {2}".format(self.first_name, self.second_name, self.username)

