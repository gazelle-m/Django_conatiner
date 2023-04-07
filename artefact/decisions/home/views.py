from django.shortcuts import render

# My imports
# from django.http import HttpResponse
from datetime import datetime


# Create your views here. THIS IS MY OWN CODE
def home(request):
    """Tesing the templates of Django"""
    # return HttpResponse('hello, world!') # Testing with HttpResponse package
    return render(request, 'home/welcome.html', {'today': datetime.today()})

def intro(request):
    """The Games introduction"""