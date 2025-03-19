from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'sitepages/about.html')


def contact(request):
    return render(request, 'sitepages/contact.html')


def privacy(request):
    return render(request, 'sitepages/privacy.html')
