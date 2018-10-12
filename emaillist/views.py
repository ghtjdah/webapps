from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from emaillist import models

# Create your views here.

def index(request):
    results = models.fetchall('emaillist')
    data = {'email_list':results}
    print('email : ',results)
    return render(request, 'emaillist/index.html',data)


def form(request):
    return render(request, 'emaillist/form.html')


def add(request):
    first_name = request.POST['fn']
    last_name = request.POST['ln']
    email = request.POST['email']

    print(type(first_name),first_name)

    emaildata = {'first_name':first_name, 'last_name':last_name, 'email':email}

    return HttpResponseRedirect('/emaillist/index')
