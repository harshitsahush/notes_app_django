from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("<int:note_id>/", views.full_note,name = "note_detail"),
]
