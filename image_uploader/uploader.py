import os
from project.settings import MEDIA_ROOT, BASE_DIR


class Uploader:

    @staticmethod
    def get_or_create_path(name):
        try:
            os.mkdir(str(name))
        except Exception as e:
            print(e)
        finally:
            return str(name)

    @staticmethod
    def get_path(owner, owner_type, picture_type, filename, base_for_file=''):
        os.chdir(MEDIA_ROOT)
        os.chdir(Uploader.get_or_create_path(owner_type))
        os.chdir(Uploader.get_or_create_path(owner))
        if picture_type:
            os.chdir(Uploader.get_or_create_path(picture_type))
        if base_for_file:
            os.chdir(Uploader.get_or_create_path(base_for_file))
        return os.getcwd() + '/' + filename
