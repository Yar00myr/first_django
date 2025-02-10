from django.urls import path
from .views import first_django, one_post


app_name = "blog"

urlpatterns = [
    path("first_start/", first_django, name="first"),
    path("one_post/<int:post_id>/", one_post, name="one_post"),
]
