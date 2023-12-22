from django.shortcuts import redirect, render
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import check_password
from connect2 import settings
from django.core.mail import send_mail

# Create your views here.

# global signal
# signal=False

def home(request):
    fname=None
    return render(request, 'landing.html',{'firstname':fname})

def signup(request):
    if request.method == 'POST':
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        gender=request.POST['gender']
        email=request.POST['email']
        pass1=request.POST['password']

        if User.objects.filter(email=email):
            messages.error(request,'Email already in use!')
            return redirect('home')


        my_user=User.objects.create_user(email=email,password=pass1, username = email)
        print(my_user.password)
        my_user.first_name=firstname
        my_user.last_name=lastname
        my_user.save()

        messages.success(request,'Your account has been successfuly created')

        #Welcome EMAIL
        subject = 'Welcome to Connect'
        message = 'Hello ' + my_user.first_name + '! \n' + 'Thanks for registering on Connect Web Application  \n\n  -- Team Connect'
        from_email = settings.EMAIL_HOST_USER
        to_list = [my_user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=False)


        return redirect('home')

    return render(request, r"C:\Users\akshi\OneDrive\Desktop\codeclause projects\Connect2\connect2\templates\signupfile.html")


# def sign():
#     global signal
#     signal=True



def signin(request):
    if request.method == 'POST':
        email1=request.POST['email']
        password1=request.POST['password']
        # print(email1,password1)
        # print((password1))
        user= User.objects.get(email=email1)


        if check_password(password1, user.password):
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            # global signal
            # signal = True
            login(request,user)
            messages.success(request,"Correct Credentials")
            fname=user.first_name

            return render(request, 'landing.html', {'firstname':fname})

        else:
            messages.error(request,'Wrong Credentials')
            return redirect('home')

    return render(request, r"C:\Users\akshi\OneDrive\Desktop\codeclause projects\Connect2\connect2\templates\loginfile.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged Out successfully")
    return redirect('home')


