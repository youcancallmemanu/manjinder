from curses.ascii import isalnum
from multiprocessing import context
from django.http import HttpRequest
from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib.auth import authenticate,login,logout
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def home(request):
    allPosts = Post.objects.all()
    print(allPosts)
    context ={ 'allPosts':allPosts}
    return render(request,'home/home.html',context)

def about(request):
    messages.success(request,'Welcome to about')
    return render(request,'home/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    


        
    return render(request,'home/contact.html')


def search(request):
    query=request.GET['query']
    if len(query)>80:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPostsauthor = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent,allPostsauthor)
    
    if allPosts.count()==0:
        messages.warning(request, "Please check your spelling")


    params = {'allPosts':allPosts,'query':query}
    return render(request,'home/search.html',params)

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return redirect('home')
        if len(username)>10:
            messages.error(request,"Username must be 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request,"User name should only contain numbers and letters")

        if pass1 != pass2:
            messages.error(request,"Password must be same in both fields")
            return redirect('home')


        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your iCoder account has been created")
        return redirect('home')

    else:
        return HttpResponse('404 Not found')



def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username=loginusername,password=loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully login")
            return redirect('home')
        else:
            messages.error(request,'Invaild credentials')
            return redirect('home')
    return HttpResponse('404-Not found')

    




def handleLogout(request):
    logout(request)
    messages.success(request,"Successfuly logout")
    return redirect('home')
    