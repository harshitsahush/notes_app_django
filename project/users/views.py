from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from .models import User


def user_login(request):
    #login and redirect to notes/
    if(request.method == "POST"):
        form = LoginForm(request.POST)
        if(form.is_valid()):
            u_name = form.cleaned_data["username"]
            pwd = form.cleaned_data["password"]
            
            #now check if username and password are a valid match in DB
            try:
                t = User.objects.get(username = u_name)
                if(t.password == pwd):
                    #store user_id in session
                    request.session["user_id"] = t.pk
                    return redirect("/notes/")

                else:
                    return render(request, 'login_form.html', {"form" : form, "message" : "Recheck username and password"})
                
            except User.DoesNotExist:
                return render(request, 'login_form.html', {"form" : form, "message" : "Recheck username and password"})
                
    else:
        form = LoginForm()

    return render(request, 'login_form.html', {"form" : form, "message" : None})
    

def user_signup(request):
    #signup and redirect to login
    if(request.method == "POST"):
        form = SignupForm(request.POST)
        if(form.is_valid()):
            u_name = form.cleaned_data["username"]
            pwd = form.cleaned_data["password"]
            
            #now check if username already exists in DB
            try:
                t = User.objects.get(username = u_name)
                return render(request, 'signup_form.html', {"form" : form, "message" : "Username already exists. Choose another."})
                
            except User.DoesNotExist:
                new_user = User()
                new_user.username = u_name
                new_user.password = pwd
                new_user.save()
                return render(request, 'signup_form.html', {"form" : form, "message" : "New user created successfully. Proceed to login page."})
        
    else:
        form = SignupForm()

    return render(request, 'signup_form.html', {"form" : form, "message" : None})


def user_signout(request):
    request.session.flush()
    return redirect("/users/login/")