from django.shortcuts import render

# Create your views here.
def landing_main(request):
    return render(request, "main.html")