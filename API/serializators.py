from rest_framework import serializers

from API.models.account import Account
from API.models.company import Company
from API.models.news import News
from API.models.picture import Picture


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['local_url', 'id']


class CompanySerializer(serializers.ModelSerializer):
    avatar = PictureSerializer(required=False)

    class Meta:
        model = Company
        fields = ['name', 'avatar', 'id']


class AccountSerializer(serializers.ModelSerializer):
    company = CompanySerializer(required=False)
    avatar = PictureSerializer(required=False)

    class Meta:
        model = Account
        fields = ['name', 'company', 'avatar', 'id']


class NewsSerializer(serializers.ModelSerializer):
    image = PictureSerializer(required=False)

    class Meta:
        model = News
        fields = ['name', 'text', 'image', 'company', 'account', 'id']
