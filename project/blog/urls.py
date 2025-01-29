from django.urls import path
from .views import first_django


app_name = "blog"

urlpatterns = [
    path("first_start/", first_django, name="first"),
]
