from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from blog.models import Post, Subject, Avatar
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from blog.forms import UserRegisterForm, UserEditForm


# Create your views here.
def index(request):
    latestPost = Post.objects.all().order_by('-id')[:3]
    formattedPost = []

    for post in latestPost:
        if post.visible:
            formattedPost.append({'id': post.id, 'name': post.name, 'body': post.body[0:250], 'image': post.image})

    return render(request, "blog/home.html", {'posts': formattedPost})


def aboutUs(request):
    return render(request, "blog/about.html")


def searchPost(request):
    post = Post.objects.filter(name__icontains=request.GET['search'])
    return render(request, "blog/display/searchPost.html", {'posts': post})


def createPost(request):
    return render(request, "blog/create/post.html")


def viewPage(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/display/post.html", {'post': post, 'date': post.creation_date})


def allPages(request):
    allPosts = Post.objects.all()
    formattedPost = []

    totalPost = len(allPosts)

    for post in allPosts:
        if post.visible:
            formattedPost.append({'id': post.id, 'name': post.name, 'body': post.body[0:250], 'image': post.image})

    return render(request, "blog/display/allPages.html", {'posts': formattedPost, 'totalPost': totalPost})


@login_required
def insertPost(request):
    subjectObj = Subject.objects.get(pk=1)
    user = User.objects.get(id=request.user.id)
    newPost = Post(name=request.POST['name'], subtitle=request.POST['subtitle'], body=request.POST['body'],
                   image=request.POST['image'], subject=subjectObj, author=user, visible=1)
    newPost.save()
    return index(request)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return index(request)
            else:
                return render(request, "blog/auth/login.html",
                              {"message": "Oops Something went wrong, please check your credentials."})
        else:
            return render(request, "blog/auth/login.html",
                          {"message": "Oops Something went wrong, please check your credentials."})

    form = AuthenticationForm()

    return render(request, "blog/auth/login.html", {'form': form})


def register(request):
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "blog/home.html", {"message": "User Created"})

    else:
        form = UserRegisterForm()

    return render(request, "blog/auth/register.html", {"form": form})


@login_required
def myPosts(request):
    posts = Post.objects.all().filter(author_id=request.user.id)
    totalPost = len(posts)
    return render(request, "blog/display/myPosts.html", {'posts': posts, 'totalPost': totalPost})


@login_required
def modifyPost(request, id):
    post = Post.objects.get(id=id)

    if request.method == 'POST':
        post.name = request.POST['name']
        post.subtitle = request.POST['subtitle']
        post.body = request.POST['body']
        post.image = request.POST['image']
        post.save()

    return render(request, "blog/edit/post.html", {"post": post})


@login_required
def deletePost(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return index(request)


@login_required
def logout_view(request):
    logout(request)
    return index(request)


@login_required
def showProfile(request):
    myForm = UserEditForm(
        initial={'firstName': request.user.first_name, 'lastName': request.user.last_name, 'email': request.user.email})
    return render(request, "blog/auth/editProfile.html", {"myForm": myForm, "user": request.user, 'status': False})


@login_required
def editProfile(request):
    user = request.user
    myForm = UserEditForm(request.POST)
    status = False

    if myForm.is_valid():
        user.email = myForm.cleaned_data['email']
        user.password1 = myForm.cleaned_data['password1']
        user.password2 = myForm.cleaned_data['password1']
        status = True
        user.save()

    return render(request, "blog/auth/editProfile.html", {"myForm": myForm, "user": request.user, 'status': status})


@login_required
def addProfileIcon(request):
    if request.method == 'POST':

        miFormulario = AvatarFormulario(request.POST, request.FILES)  # aquí mellega toda la información del html

        if miFormulario.is_valid:  # Si pasó la validación de Django

            u = User.objects.get(username=request.user)

            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])

            avatar.save()

            return render(request, "AppCoder/inicio.html")  # Vuelvo al inicio o a donde quieran

    else:

        miFormulario = AvatarFormulario()  # Formulario vacio para construir el html

    return render(request, "AppCoder/agregarAvatar.html", {"miFormulario": miFormulario})
