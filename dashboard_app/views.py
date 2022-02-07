from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, 'home.html')

def notes (requst):
     return render(requst, 'notes.html')   