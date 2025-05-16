from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def experience(request):
    return render(request, 'experience.html')

def skill(request):
    return render(request, 'skill.html')