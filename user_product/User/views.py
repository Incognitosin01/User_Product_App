from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth,User
from django.urls import reverse
from django.contrib.auth import login,logout
from django.contrib import messages
from .forms import PostForm
from .models import Post
# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        f_name=request.POST.get('first_name')
        l_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        new_user = User.objects.db_manager('User_db').create_user(username=username, first_name=f_name, last_name=l_name,password=password,email=email)
        new_user.save()
        messages.success(request,"Please sign in with registered credentials")
        return redirect('sign_in')
    else:
        return render(request,"html/register.html")

def sign_in(request):
    if request.method == 'GET':
        return render(request, 'html/sign_in.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("index")
        return HttpResponse('<h1>Sorry, no such user</h1>')

@login_required(login_url='sign_in')
def sign_out(request):
    if request.user.is_anonymous:
        return HttpResponse("<h1>BAD WAY REQUEST</h1>")
    logout(request)
    messages.error(request,"Successfully Logout !")
    return redirect(reverse('sign_in'))

@login_required(login_url='sign_in')
def index(request):
    if request.method == "GET":
        form = PostForm
        return render(request,'html/index.html',{'form':form})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            text = form.cleaned_data['text']
            data = Post(user=user,text=text)
            data.save()
            messages.success(request,"Post created Successfully !")
            return redirect('index')
        else:
            messages.error(request,"Invalid Data provided !")
            return redirect('index')

    