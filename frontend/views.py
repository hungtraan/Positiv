from django.shortcuts import render

def home(request):
    return render(request, 'home-positiv.html', {})

def diary(request):
    return render(request, 'entries.html', {})
    
def graphs(request):
    return render(request, 'graphs.html', {})
    
def profile(request):
    return render(request, 'profile.html', {})
