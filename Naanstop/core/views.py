from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-id')[:5]
    return render(request, "core/home.html", {"posts": posts})
