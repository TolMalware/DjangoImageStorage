from rest_framework import mixins, viewsets

from API.models.account import Account
from API.models.company import Company
from API.models.news import News
from API.serializators import AccountSerializer, CompanySerializer, NewsSerializer


class AccountView(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class CompanyView(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class NewsView(mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.ListModelMixin,
               viewsets.GenericViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
