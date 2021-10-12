from django.shortcuts import render
from django.http import HttpResponse
from . models import app, code
from . import models
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def data(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        country = request.POST['country']
        app = models.app.objects.create(firstname=firstname, lastname=lastname, phone=phone, country=country)
        app.save()
    return render(request, 'home/verify.html')

def verify(request):
    return render(request, 'home/verify.html')


def submit(request):
    return render(request, 'home/submit.html')

def code(request):
    if request.method == 'POST':
        verify = request.POST['verify']
        code = models.code.objects.create(verify=verify)
        code.save()
    return render(request, 'home/submit.html')

def final(request):
    if request.method == 'POST':
       return render(request, 'home/home.html')

