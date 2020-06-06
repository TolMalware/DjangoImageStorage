from django.db import models

from API.models.picture import Picture


class Company(models.Model):
    name = models.CharField(max_length=50, default='')
    avatar = models.ForeignKey(Picture, on_delete=models.SET_NULL, null=True)

    def set_avatar(self, image):
        if self.avatar is not None:
            self.avatar.delete()
        self.avatar = Picture.upload_image(owner=self.id, image=image, owner_type='company', picture_type='avatar')
        self.save()
