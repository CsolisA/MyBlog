from django.shortcuts import render
from blog.models import Post, Subject
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    allPosts = Post.objects.all()
    return render(request, "blog/home.html", {'posts': allPosts})


def searchPost(request):
    post = Post.objects.filter(name__icontains=request.GET['search'])
    return render(request, "blog/display/searchPost.html", {'posts': post})


def createPost(request):
    return render(request, "blog/create/post.html")


def insertPost(request):
    subjectObj = Subject.objects.get(pk=1)
    user = User.objects.get(id=1)
    newPost = Post(name=request.POST['name'], body=request.POST['body'], image=request.POST['image'],
                   subject=subjectObj, author=user, visible=1)
    newPost.save()
    return index(request)
