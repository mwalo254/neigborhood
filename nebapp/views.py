#from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Profile,Neighbourhood,Business,Post,Location,Comment
from .forms import NewHoodForm,NewBusinessForm,NewPostForm,NewCommentForm,NewProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import status



@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    date = dt.date.today()
    hoods = Neighbourhood.objects.all()
 
    return render(request, 'users/index.html',{'date':date, 'hoods':hoods})


@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    title= "Profile"
    user_profile= Profile.objects.filter(user=current_user)
    hoods = Neighbourhood.objects.all()
    if len(user_profile)<1:
        user_profile='No profile info'

    else:
        user_profile= Profile.objects.get(user=current_user)


    return render(request, 'users/user_profile.html', { 'user_profile':user_profile, 'hoods':hoods, 'title':title})


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    
    if request.method == 'POST':
        form=NewProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            profile=form.save(commit=False)
            profile.user = current_user
            profile.save()

            return redirect('user-profile')

    else:
            form=NewProfileForm(instance=request.user)

    return render(request, 'users/edit_profile.html', {'form':form})


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'hood' in request.GET and request.GET['hood']:
        search_term= request.GET.get('hood')
        searched_hoods=Neighbourhood.search_by_title(search_term)
        message=f'{search_term}'

        return render(request,'users/search.html',{'message':message,'hood':searched_hoods})

    else:
        message="You haven't searched for any neighbourhood"
        return render(request, 'users/search.html',{'message':message})


@login_required(login_url='/accounts/login/')
def create_hood(request):
    current_user = request.user
    if request.method =='POST':
        form = NewHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = current_user
            hood.save()
        return redirect('welcome')

    else:
        form = NewHoodForm()
    return render(request, 'users/new_hood.html', {'form':form})


@login_required(login_url='/accounts/login/')
def search_business(request):
    if 'business' in request.GET and request.GET['business']:
        search_term= request.GET.get('business')
        searched_business=Business.search_by_title(search_term)
        message=f'{search_term}'

        return render(request,'users/search_business.html',{'message':message,'business':searched_business})

    else:
        message="You haven't searched for any business"
        return render(request, 'users/search.html',{'message':message})





def location(request):
    date = dt.date.today()
    return render(request, 'users/location.html',{"date":date})


@login_required(login_url='/accounts/login/')
def my_hood(request,id):
    date = dt.date.today()
    current_user = request.user
    our_hood=Neighbourhood.objects.get(id=id)
    posts=Post.objects.filter(hood=our_hood)
    business=Business.objects.filter(hood=our_hood)
    return render(request, 'users/hood.html',{'our_hood':our_hood, 'posts':posts,'business':business,'date':date})



@login_required(login_url='/accounts/login/')
def new_bussiness(request,id):
    date = dt.date.today()
    current_user = request.user
    our_hood = Neighbourhood.objects.get(id=id)
    business= Business.objects.filter(hood=our_hood)
    form = NewBusinessForm()
    if request.method =='POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit = False)
            business.user = current_user
            business.hood = our_hood
            business.save()
            
            return redirect(request, 'my-hood')

    else:
        form = NewBusinessForm()
        return render(request, 'users/business.html', {'form':form,'business':business,'our_hood':our_hood,'date':date})


@login_required(login_url='/accounts/login/')
def new_post(request,id):
    date = dt.date.today()
    current_user = request.user
    hoods = Neighbourhood.objects.get(id=id)
    comments = Comment.objects.filter(post=id).order_by('-pub_date')
    posts=Post.objects.filter(hood=hoods)
    form = NewPostForm()

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user=current_user.user
            post.hood = hood
            post.save()
                    
            return redirect('my-hood')

    else:
        form= NewPostForm()
        return render(request, 'users/post.html', {'form':form, 'date':date,'hoods':hoods,'posts':posts,'comments':comments})

@login_required(login_url='/accounts/login/')
def new_comment(request,id):
    current_user=request.user

    try:
        comments = Comment.objects.filter(post_id=id)
    except:
        comments = []
    posts= Post.objects.get(id=id)
    if request.method =="POST":
        form = NewCommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.post = posts
            comment.save()
    else:
        form = NewCommentForm()

    return render(request, 'users/comment.html',{'post':post,"comments":comments,"form":form})