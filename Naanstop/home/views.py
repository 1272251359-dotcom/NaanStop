from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post, Comment

def index(request):
    posts = Post.objects.all().order_by('-created_at')[:5]
    return render(request, 'home/index.html', {'posts': posts})

def load_more_posts(request):
    offset = int(request.GET.get("offset", 0))
    limit = 5
    posts = Post.objects.all().order_by('-created_at')[offset:offset + limit]
    return render(request, 'home/post_list.html', {'posts': posts})

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    return JsonResponse({'likes': post.likes})

def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        name = request.POST.get('name')
        text = request.POST.get('text')
        if name and text:
            Comment.objects.create(post=post, name=name, text=text)
        return redirect('index')
