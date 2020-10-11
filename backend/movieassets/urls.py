from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'characters', views.sync_views.CharacterListView)

app_name = 'movieassets'
urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'api/fetch-data/', views.async_views.fetch_data_view, name='fetch_data_view'),
]
