from django.shortcuts import render

# Create your views here.
def user_profile(request):
    return render(request, "profile.html")

def sign_up_1(request):
    return render(request, "signup1.html")

def sign_up_2(request):
    return render(request, "signup2.html")

def sign_up_3(request):
    return render(request, "signup3.html")

def sign_up_4(request):
    return render(request, "signup4.html")

def login(request):
    return render(request, "login.html")
