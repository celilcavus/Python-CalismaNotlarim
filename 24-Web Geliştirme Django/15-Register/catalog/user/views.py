from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if (user is not None):
            auth.login(request=request, user=user)
            messages.add_message(request,messages.SUCCESS,'Oturm Acildi')
            return redirect('index')
        else:
            messages.add_message(request,messages.ERROR,'Giriş Başarisiz')
            return render(request, 'user/login.html')
    else:
        return render(request, 'user/login.html')

def register(request):
    if request.method == 'POST':

        # get form values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            # Username
            if User.objects.filter(username=username).exists():
                messages.add_message(request,messages.WARNING,'Bu username daha önce alinmiş')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(request,messages.WARNING,'Bu email daha önce alinmiş')
                    return redirect('register')
                else:
                    # her şey güzel
                    user = User.objects.create_user(
                        username=username, password=password, email=email)
                    user.save()
                    messages.add_message(request,messages.INFO,'Kullanici Oluşturuldu.')
                    return redirect('login')
        else:
            messages.add_message(request,messages.WARNING,'Kullanici Oluşuturulamadi.')
            return redirect('register')
    else:
        return render(request, 'user/register.html')


def logout(request):
    return render(request, 'user/logout.html')
