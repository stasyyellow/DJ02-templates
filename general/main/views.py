from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html', {'caption':"DjangoCatProject"})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def services(request):
    return render(request, 'main/services.html')
