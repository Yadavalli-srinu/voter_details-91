from django.shortcuts import render,redirect

from django.shortcuts import render,redirect
from app1.models import voter_user_model,voter_profile_model
from app1.forms import user_form1,profile_form1
from app1.forms1 import user_form2,profile_form2
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def register_form(request):
   message=''
   if request.method=="POST":
      username=request.POST.get("reg_username")
      useremail=request.POST.get("reg_useremail")
      p1=request.POST.get("reg_userpassword")
      p2=request.POST.get("reg_userconpassword")

      if p1!=p2:
         message="Please Enter Valid Password"

      elif User.objects.filter(email=useremail).exists():
         message="Email Already Exists"
      else:
         user=User.objects.create_user(username=username,email=useremail,password=p1)
         user.save()
         message="User Create Successfully"
         return redirect("log101")
   return render(request,"frontend_app1/reg.html",{"message": message})
      
def login1_form(request):
    message = ""

    if request.method == "POST":
        username = request.POST.get("log_userneme")
        password = request.POST.get("log_userpassword")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home101")   
        else:
            message = "Invalid Username or Password"

    return render(request,"frontend_app1/login.html",{"message": message})

def home(request):
   return render(request,'frontend_app1/home.html')





def voter_user_table(request):
    data=voter_user_model.objects.all()
    content={
        "data":data
    }
    return render(request,"frontend_app1/user_table.html",content)

def voter_user_empty_form(request):
    form=user_form1()
    if request.method=="POST":
        form=user_form1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usertable')
    else:
        form=user_form1()
        content={
            "form":form
        }
        return render(request,"frontend_app1/user_form.html",content)


def voter_user_update_form(request,id):
    data=voter_user_model.objects.get(id=id)
    if request.method=="POST":
        form=user_form2(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('usertable')
    else:
        form=user_form2(instance=data)
        content={
            "form":form
        }
        return render(request,"frontend_app1/user_u_form.html",content)
    
def voter_user_delete(requst,id):
    data=voter_user_model.objects.get(id=id)
    data.delete()
    return redirect("usertable")


def voter_profile_table(request):
    data=voter_profile_model.objects.all()
    content={
        "data":data
    }
    return render(request,"frontend_app1/profile_table.html",content)


def voter_profile_empty_form(request):
    form=profile_form1()
    if request.method=="POST":
        form=profile_form1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profiletable')
    else:
        form=profile_form1()
        content={
            "form":form
        }
        return render(request,"frontend_app1/profile_form.html",content)


def voter_profile_update_form(request,id):
    data=voter_profile_model.objects.get(id=id)
    if request.method=="POST":
        form=profile_form2(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('profiletable')
    else:
        form=profile_form2(instance=data)
        content={
            "form":form
        }
        return render(request,"frontend_app1/profile_u_form.html",content)
    
def voter_profile_delete(requst,id):
    data=voter_profile_model.objects.get(id=id)
    data.delete()
    return redirect("profiletable")
