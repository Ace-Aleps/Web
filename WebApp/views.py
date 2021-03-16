from django.shortcuts import render

def homepage(request):
    return render(request, 'WebApp/home.html')

def portfolio(request):
    return render(request, 'WebApp/portfolio.html', {'title':'Portfolio'})

def about(request):
    return render(request, 'WebApp/about.html', {'title':'About'})
