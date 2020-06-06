import os
import uuid

from PIL import Image
from django.db import models
from resizeimage import resizeimage

from image_uploader.uploader import Uploader


def upload_to(instance, filename):
    relative_path = instance.url_to_upload.rfind('images/') + len("images/")
    return instance.url_to_upload[relative_path:]


class Picture(models.Model):
    local_url = models.ImageField(upload_to=upload_to)
    url_to_upload = models.CharField(max_length=200, default='')

    @staticmethod
    def upload_image(owner, owner_type, picture_type, image, base=""):
        image_name = Picture.get_uuid_name_with_extension(image)
        picture = Picture.objects.create(
            local_url=image,
            url_to_upload=Uploader.get_path(owner, owner_type, picture_type, image_name, base_for_file=base))
        return picture

    def delete(self, using=None, keep_parents=False):
        os.remove(self.url_to_upload)
        super().delete(using=using, keep_parents=keep_parents)

    @staticmethod
    def get_uuid_name_with_extension(image):
        img = Image.open(image)
        uuid_name = uuid.uuid4()
        return f'{uuid_name}.{img.format.lower()}'
