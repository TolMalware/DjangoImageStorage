from django.urls import path, include
from rest_framework import routers

from API.views import AccountView, CompanyView, NewsView

router = routers.DefaultRouter()
router.register(r'account', AccountView)
router.register(r'company', CompanyView)
router.register(r'news', NewsView)
urlpatterns = [
    path('', include(router.urls))
]
