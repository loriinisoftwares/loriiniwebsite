from django.shortcuts import render


def home(request):
    return render(request, 'sample/home.html', {'title' : 'Home'})

def about(request):
    return render(request, 'sample/about.html', {'title' : 'About'})
