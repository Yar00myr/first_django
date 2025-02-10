from django.shortcuts import render, get_object_or_404
from .models import Post, Comment


def first_django(request):
    posts = Post.objects.all()
    data = {"posts": posts}
    return render(request, "index.html", context=data)


def one_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    data = {"post": post}
    return render(request, "post.html", context=data)
