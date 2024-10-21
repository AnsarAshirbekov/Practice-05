from django.shortcuts import render

def index(request):
    return render(request, 'about_me.html')

def skills(request):
    return render(request, 'skills.html')

def portfolio(request):
    return render(request, 'portfolio.html')
