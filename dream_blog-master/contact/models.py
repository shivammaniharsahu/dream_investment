from __future__ import unicode_literals
from django.db import models


class Students(models.Model):
    full_name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_number = models.IntegerField()
    message = models.CharField(max_length=200)
    class Meta:
        db_table = "students"

    def __str__(self):  # __unicode__ on Python 2
        return self.full_name
