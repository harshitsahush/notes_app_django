from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    #redirect to /notes/
    return redirect("/notes/")