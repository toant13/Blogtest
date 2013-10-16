# Create your views here.
from django.shortcuts import render

from blogapp.models import Post

def index(request):
    latest_blog_list = Post.objects.order_by('-created')[:5]
    context = {'latest_blog_list': latest_blog_list}
    return render (request, 'blogmain/content.html', context)