from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404
# Create your views here.
# render list view of all post
def post_list(request):
    """" get all the list from object manager and send them to the html template """
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})
# detail page∂
def post_detail(request, id):
    """ If the posts exists then render the page otherwise show 404 error"""
    post = get_object_or_404(Post, id=id, status= Post.Status.PUBLISHED)
    return render(request, 'body/post/detail.html', {'post': post})


