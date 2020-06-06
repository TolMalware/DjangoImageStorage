import os

from django.contrib.auth.models import User
from django.db import models

from API.models.company import Company
from API.models.picture import Picture


class Account(models.Model):
    name = models.CharField(max_length=50, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    avatar = models.ForeignKey(Picture, on_delete=models.SET_NULL, null=True)

    def set_avatar(self, image):
        if self.avatar is not None:
            self.avatar.delete()
        self.avatar = Picture.upload_image(owner=self.id, image=image, owner_type='account', picture_type='avatar')
        self.save()
