from django.shortcuts import render, get_object_or_404
from .models import Post, Group

# Create your views here.

def index(request):
    """YaTube - main."""
    TEMPLATE = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts' : posts
    }
    return render(request, TEMPLATE, context)

def group_posts(request, slug):
    """YaTube - page group_posts."""
    TEMPLATE = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, TEMPLATE, context)