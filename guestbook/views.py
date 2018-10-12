from django.http import HttpResponseRedirect
from django.shortcuts import render
from guestbook import models

# Create your views here.

def index(request):
    messages = models.fetchall('guestbook')
    data = {'messages':messages}

    return render(request, 'guestbook/index.html', data)


def deleteform(request):
    no = request.GET['no']
    data = {'no':no}
    return render(request, 'guestbook/deleteform.html',data)


def add(request):
    name = request.POST['name']
    password = request.POST['password']
    message = request.POST['content']

    data = {'name': name, 'password': password, 'message':message}

    models.insert(data)

    return HttpResponseRedirect("/guestbook/")

def delete(request):
    no = request.POST['no']
    password = request.POST['password']
    data = {'no':no, 'password':password}
    models.delete(data)

    return HttpResponseRedirect("/guestbook/")