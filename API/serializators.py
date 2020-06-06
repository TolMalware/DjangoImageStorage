from rest_framework import serializers

from API.models.account import Account
from API.models.company import Company
from API.models.news import News


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'id']


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Account
        fields = ['name', 'company', 'id']


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    company = CompanySerializer()
    account = AccountSerializer()

    class Meta:
        model = News
        fields = ['name', 'company', 'id', 'account', 'text']
