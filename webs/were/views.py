from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from .forms import CreateUserForm

def black(request):
    return render(request, "templates/black.html")

def login(request):
    return render(request, "templates/login.html")

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, "templates/register.html")

def home(request):
    return render(request, "templates/home.html")

def gallery(request):
    return render(request, "templates/gallery.html")

def designer(request):
    return render(request, "templates/designer.html")

def contacts(request):
    return render(request, "templates/contacts.html")

