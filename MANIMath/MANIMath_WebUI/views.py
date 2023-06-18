from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from .models import *

def home(request: HttpRequest):
    return render(request,
        'MANIMath_WebUI/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )

def topic_list(request):
    topics = Topic.objects.all()
    categories = Category.objects.all()

    query = request.GET.get('q', '')
    category = request.GET.get('category', '')

    if query:
        topics = topics.filter(name__icontains=query)
        categories = categories.filter(name__icontains=query)

    if category:
        topics = topics.filter(category__name=category)  

    return render(
        request, 
        'MANIMath_WebUI/topics.html',
        {
            'title': 'Topics',
            'year': datetime.now().year,
            'topics': topics,
            'categories': categories,
            'query': query
        }
    )
