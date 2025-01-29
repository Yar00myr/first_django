from django.shortcuts import render


def first_django(request):
    return render(request, "index.html")
