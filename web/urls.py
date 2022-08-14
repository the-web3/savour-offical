from django.urls import path
from web.views import index


urlpatterns = [
    path(r"", index, name="index"),
]