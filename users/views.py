from django.shortcuts import render,redirect
from users.forms import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import *

def loginuser(request):
    if request.user.is_authenticated and request.user.is_superuser:        
        messages.warning(request, f' You are already logged in !!')
        return redirect('/home')
    elif request.user.is_authenticated and request.user.is_lecturer:
        messages.warning(request, f' You are already logged in !!')
        return redirect('/staff_home')
    elif request.user.is_authenticated and request.user.is_student:
        messages.warning(request, f' You are already logged in !!')
        return redirect('/student_home')
    else:        
        if request.method == 'POST':            
            email = request.POST['email']
            password = request.POST['password']
           
            user = authenticate(request, email = email, password = password)
            if user is not None:
                form = login(request, user)                
                messages.success(request, f' welcome {email} !')
                path_redirect = request.get_full_path().split('?next=',1)
                if '?next=' in request.get_full_path():
                    return redirect(path_redirect[1])
                else:
                    # return redirect('/')    
                    if user.is_superuser:
                        return redirect("home")
                    elif user.is_lecturer:
                        return redirect("staff_home")
                    elif user.is_student:
                        return redirect("student_home")                 
                
            else:
                messages.error(request, f'Invalid details, please enter correct details or sign up!')
        form = LoginForm()       
    return render(request, 'accounts/login.html', {'form':form})


def logoutuser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out successfully")
    return redirect('/')

