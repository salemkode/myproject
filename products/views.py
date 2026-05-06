from django.shortcuts import render

def home(request):
    return render(request, 'products/home.html')

def about(request):
    return render(request, 'products/about.html')