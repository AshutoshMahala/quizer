from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views, api

urlpatterns = [
    path("", views.index, name="index"),
    path("api/", api.api.urls),
]
