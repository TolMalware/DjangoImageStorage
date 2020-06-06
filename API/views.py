from rest_framework import mixins, viewsets
from API.models.account import Account
from API.models.company import Company
from API.models.news import News
from API.serializators import AccountSerializer, CompanySerializer, NewsSerializer


class AccountView(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def set_avatar_from_request(self, account):
        avatar = self.request.data.get('avatar')
        if avatar is not None:
            account.set_avatar(avatar)

    def perform_create(self, serializer):
        self.set_avatar_from_request(serializer.save())

    def perform_update(self, serializer):
        self.set_avatar_from_request(serializer.save())


class CompanyView(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def set_avatar_from_request(self, company):
        avatar = self.request.data.get('avatar')
        if avatar is not None:
            company.set_avatar(avatar)

    def perform_create(self, serializer):
        self.set_avatar_from_request(serializer.save())

    def perform_update(self, serializer):
        self.set_avatar_from_request(serializer.save())


class NewsView(mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.ListModelMixin,
               mixins.CreateModelMixin,
               viewsets.GenericViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def set_image_from_request(self, news):
        image = self.request.data.get('image')
        if image is not None:
            news.set_image(image)

    def perform_create(self, serializer):
        self.set_image_from_request(serializer.save())

    def perform_update(self, serializer):
        self.set_image_from_request(serializer.save())
