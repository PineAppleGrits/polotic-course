from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import *


# Create your views here.

def registrarse(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {
        'form': form
    })
