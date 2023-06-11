from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime

def home(request: HttpRequest):
    return render(request,
        'MANIMath_WebUI/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )