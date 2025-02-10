from django.urls import path
from .views import home, one_post, create_post


app_name = "blog"

urlpatterns = [
    path("home/", home, name="home"),
    path("one_post/<int:post_id>/", one_post, name="one_post"),
    path("create_post/", create_post, name="create_post"),
]
