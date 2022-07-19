from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(request):
    """YaTube - main."""
    return HttpResponse('Main page of the YaTube service.')

def group_posts(request, slug):
    """Posts filtered by groups."""
    return HttpResponse(f'My posts {slug}')