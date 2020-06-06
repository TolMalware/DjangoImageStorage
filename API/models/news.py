from django.db import models

from API.models.account import Account
from API.models.company import Company
from API.models.picture import Picture


class News(models.Model):
    name = models.CharField(max_length=50, default='')
    text = models.TextField(default='')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=None)
    image = models.ForeignKey(Picture, on_delete=models.SET_NULL, null=True)

    def set_image(self, image):
        if self.image is not None:
            self.image.delete()
        self.image = Picture.upload_image(owner=self.company.id, image=image, owner_type='company',
                                          picture_type='news', base=self.id)
        self.save()
