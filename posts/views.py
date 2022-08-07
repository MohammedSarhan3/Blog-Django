from django.shortcuts import render

# Create your views here.

from .models import Post

def all_posts(request):
    posts = Post.objects.all()
    return render( request, 'posts.html',{'mahmoud':posts} )


def single_post(request,id):
    post = Post.objects.get(id=id)
    return render(request, 'single.html',{'single_post':post})