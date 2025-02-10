from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import Post, Comment


def home(request):
    posts = Post.objects.all()
    data = {"posts": posts}
    return render(request, "index.html", context=data)


def one_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    data = {"post": post}
    return render(request, "post.html", context=data)


def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = get_object_or_404(User)
        try:
            post = Post(title=title, content=content, author=author)
            post.full_clean()
        except:
            return HttpResponse("<h1>Bad values</h1>")
        else:
            post.save()
        return redirect("blog:home")
    return render(request, "create_post.html")
