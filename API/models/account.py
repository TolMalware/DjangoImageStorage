from django.contrib.auth.models import User
from django.db import models

from API.models.company import Company


class Account(models.Model):
    name = models.CharField(max_length=50, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=None)
