from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from django.db.models import Q
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

    category = request.GET.get('category', '')
    query = request.GET.get('q', '')
    if query:
        topics = topics.filter(
            Q(name__contains=query) | Q(category__name__contains=query)
        )
        categories = categories.filter(name__contains=query)       
        if not categories:
            categories = Category.objects.all()

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
