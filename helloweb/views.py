from django.shortcuts import render

# Create your views here.


def hello(request):
    #model(CRUD)
    return render(request, 'helloweb/hello.html')


def tags(request):
    return render(request, 'helloweb/tags.html')


def join(request):
    email = request.POST['email']
    passwd = request.POST['password']
    gender = request.POST['gender']
    birth_y = request.POST['birth-year']
    hobby = request.POST.getlist('hobby')
    self_intro = request.POST['self - introducing']

    data = {'email_value':email, 'password_value':passwd, 'gender_value':gender,
            'birth_y_value': birth_y, 'hobby_values':hobby, 'self_intro_value':self_intro}

    return render(request, 'helloweb/join_result.html',data)