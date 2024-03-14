from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def log_out(request):
    """""注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
    
def register(request:HttpRequest):
    """""注册新用户"""
    if request.method != "POST":
        form = UserCreationForm()
    else:
        #处理填好的表单
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user=form.save()
            #让用户自动登录,再重新定向到主页
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password'])
            login(request,authenticated_user)
            return  HttpResponseRedirect(reverse('learning_logs:index'))
    context={'form':form}
    return render(request,'users/register.html',context)