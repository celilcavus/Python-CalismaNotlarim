from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render(request,'user/login.html')

def register(request):
    if request.method == 'post':
        #user Kayit
        #get form values
        username = request.POST['username']
        mail = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if (password == repassword):
            if(User.objects.filter(username = username).exists()):
                print("Bu Kullanici Adi daha önce alinmiş.")
                return redirect('register')
            else:
                if(User.objects.filter(mail = mail).exists()):
                    print("Bu Email Daha önce alinmiş")
                    return redirect('register')
                else:
                    #kayit işlemi
                    user = User.objects.create_user(username=username,email=mail,password=password)
                    user.save()
                    print("Kullanici Oluşturuldu.")
                    return redirect('login')
        else:
            print("Parolalar eşleşmiyor.")
            return redirect('register')
    else:
        return render(request,'user/register.html')

def logout(request):
    return render(request,'user/logout.html')