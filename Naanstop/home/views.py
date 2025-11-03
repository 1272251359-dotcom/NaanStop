from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-created_at')[:5]
    return render(request, 'home/index.html', {'posts': posts})

def load_more_posts(request):
    offset = int(request.GET.get("offset", 0))
    limit = 5
    posts = Post.objects.all().order_by('-created_at')[offset:offset + limit]
    return render(request, 'home/post_list.html', {'posts': posts})
