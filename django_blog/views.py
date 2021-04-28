from django.db.models.fields.related import ForeignKey
from django.shortcuts import redirect, render, get_object_or_404
from .models import Author, Category, Article, About_Me
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django_blog import forms


# Create your views here.
# User registration system functionality here....
def User_Registration(request):
    if request.user.is_authenticated:
        return redirect('index')

    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.info(request, 'This account is created successfully!'+' '+ user)
                return redirect('login')
            else:
                messages.info(request, 'Tow password are not match!')
                
        context = {
            'form': form
        }
        return render(request, 'registration.html', context)


# User login system functionality here....
def User_Login(request):
    if request.user.is_authenticated:
        return redirect('index')

    else:
        if request.method == 'POST':
                username = request.POST.get('username')
                password= request.POST.get('password')

                user = authenticate(request, username = username, password = password)
                if user is not None:
                    login(request, user)
                    messages.info(request, 'User Login Successfull')
                    return redirect('index')

                else:
                    messages.info(request, 'username or password incorrect!')

        context={}
        return render(request, 'login.html', context)


#  User logout funtinality here.....
def getlogout(request):
    logout(request)
    messages.info(request, 'User Logout Successfull')
    return redirect('index')

# 404 functionality here....
def error_404_view(request, exception):
    return render(request,'404.html')

# index funtionality here....
def Index(request):
    author = Author.objects.all()
    aritcle = Article.objects.all()
    paginator = Paginator(aritcle, 8) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    tottal_article = paginator.get_page(page_number)

    context = {
        'author': author,
        'aritcle': tottal_article,
    }
    return render(request, 'index.html', context)


# Articale_details functionality here....
@login_required(login_url='login')
def Article_Details(request, id, slug):
    author = Author.objects.all()
    post = get_object_or_404(Article, pk = id, slug = slug)

    context = {
        'post': post,
        'author': author
    }
    return render(request, 'articles_details.html', context)


# Perticuler article category functionality here....
def Category_Post(request, name):
    author = Author.objects.all()
    aritcle = Article.objects.all()
    cat = get_object_or_404(Category, name=name)
    post = Article.objects.filter(category=cat.id)

    paginator = Paginator(post, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    tottal_article = paginator.get_page(page_number)

    
    context = {
        'author': author,
        'aritcle': aritcle,
        'post': tottal_article,
        'cat': cat
    }
    return render(request, 'category.html', context)

# aboute me funtionality here....
def Myself(request):
    author = Author.objects.all()
    about = About_Me.objects.all()
    context={
        'author': author,
        'about': about
    }
    return render(request, 'about.html', context)


# Create_article frome here......
@login_required(login_url='login')
def ArticlaeFrom(request):
    form = forms.Create_Artical()

    if request.method == "POST":
        form = forms.Create_Artical(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')

    context = {
        "form": form
    }
    return render(request, 'createArticle.html', context)


# website category show functionality....
def Show_Category(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'show_category.html', context)


#create a author functionality here....
def Create_Author(request):
    form = forms.User_Create_Author()

    if request.method == "POST":
        form = forms.User_Create_Author(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save(commit=True)
            return redirect('create-article')
    context = {
        "form": form
    }
    return render(request, 'create_author.html', context)

