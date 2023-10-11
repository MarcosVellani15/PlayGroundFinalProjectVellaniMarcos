from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . import forms
 
# Create your views here.
def index(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")

def clientes(request):
    return render(request, "cliente/index.html")

def producto(request):
    return render(request, "producto/index.html")

def login_request(request):
    if request.method == "POST":
        form = forms.CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            email = form.cleaned_data.get("email")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request,user)
                return render(request, "home/index.html", {"mensaje": "Se ha logueado correctamente."})
    else:
        form = AuthenticationForm()
    return render(request, "home/login.html", {"form": form})

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request,"home/index.html", {"mensaje": "Su usuario fue creado correctamente."})
    else:
        form = UserCreationForm()
    return render(request,"home/registro.html", {"form": form})