from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Sigil(models.Model):
    upload_date = models.DateTimeField('upload_date')
    end_date = models.DateTimeField('end_date')
    image = models.ImageField(upload_to='uploads/sigils/%Y/%m/%d/')
    title = models.CharField(max_length=200)
    intent = models.TextField()
    owner = models.ForeignKey(User)
    def __str__(self):
        return  '{} | {}'.format(self.owner.username, self.title)