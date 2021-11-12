from django.shortcuts import render

# Create your views here.
def matching_main(request):
    return render(request, "matching.html")

def request_list(request):
    return render(request, "request_list.html")