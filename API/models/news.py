from django.db import models

from API.models.account import Account
from API.models.company import Company


class News(models.Model):
    name = models.CharField(max_length=50, default='')
    text = models.TextField(default='')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=None)
