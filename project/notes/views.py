from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import NotesForm
from .models import note, User


# Create your views here.
def home(request):
    #get user_id from session
    if("user_id" in request.session):
        curr_user = User.objects.get(pk = request.session["user_id"])
    else:
        return redirect("/users/login/")


    #if form has been submitted, get the new values and add to DB
    #get all the notes from DB and render them as well
    all_notes = None
    if(request.method == "POST"):
        form = NotesForm(request.POST)
        if(form.is_valid()):
            data = form.cleaned_data
            new_note = note()
            new_note.title = data["title"]
            new_note.content = data["content"]
            new_note.username = curr_user
            new_note.save()

    # since we always want to load a fresh form, without the previously submitted data
    # else:
    #     form = NotesForm()

    form = NotesForm()
    
    #fetch all notes from DB
    all_notes = note.objects.filter(username = curr_user)

    return render(request, "all_notes.html", {"form" : form, "content" : all_notes})

def full_note(request, note_id):
    fetched_note = note.objects.get(pk = note_id)
    return render(request, "note_detail_page.html", {"note" : fetched_note})

def note_delete(request, note_id):
    #delete note
    fetched_note = note.objects.get(pk = note_id)
    fetched_note.delete()
    #now redirect to the all notes page
    return redirect("/notes/")