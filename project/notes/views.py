from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import NotesForm
from .models import note


# Create your views here.
def home(request):
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
            new_note.save()

    # since we always want to load a fresh form, without the previously submitted data
    # else:
    #     form = NotesForm()

    form = NotesForm()
    
    #fetch all notes from DB
    all_notes = note.objects.all()

    return render(request, "all_notes.html", {"form" : form, "content" : all_notes})

def full_note(request, note_id):
    fetched_note = note.objects.get(pk = note_id)
    return render(request, "note_detail_page.html", {"note" : fetched_note})