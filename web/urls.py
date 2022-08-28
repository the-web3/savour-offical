from django.urls import path
from web.views import index, join_submit


urlpatterns = [
    path(r"", index, name="index"),
    path(r"join_submit", join_submit, name="join_submit"),
]