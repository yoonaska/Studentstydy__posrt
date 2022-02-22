
from email import message
from django.shortcuts import render
from django.urls import is_valid_path
from django.contrib import messages

from .forms import *

# Create your views here.
def home (request):
    return render(request, 'home.html')


def notes (request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user,title= request.POST['title'],discrption= request.POST['discrption'])
            notes.save()
        messages.success(request,"note is added from{requst.user.username} sucessfully")

    else:
        form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes':notes,'form':form}
    return render(request, 'notes.html', context,)   

    #