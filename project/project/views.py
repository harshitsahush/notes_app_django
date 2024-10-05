from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    #check for presence of user_id in session
    #if present, redirect to notes
    #else, to login
    if("user_id" in request.session):
        return redirect("notes/")
    
    return redirect("users/login/")