import subprocess
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Q
from .models import *
from .forms import *

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

def topic_detail(request, topic_name):

    topic = get_object_or_404(Topic, name=topic_name)

    return render(
        request, 
        'MANIMath_WebUI/details.html', 
        {
            'title' : topic_name,
            'topic': topic,
        }
    )

@login_required(login_url='login')
def create_animation(request, topic_name):
    
    topic = get_object_or_404(Topic, name=topic_name)
    category = topic.category.name

    form_model_dict = {
        'Functions': {
            'form_class': FunctionForm,
            'model_class': FunctionModel,
        },
        'Root Finding Algorithms': {
            'form_class': RootFindingForm,
            'model_class': RootFindingModel,
        },
        'Sorting Algorithms': {
            'form_class': SortForm,
            'model_class': SortModel,
        },
        'Searching Algorithms': {
            'form_class': SearchForm,
            'model_class': SearchModel,
        },
    }

    if category in form_model_dict:
        form_class = form_model_dict[category]["form_class"]
        model_class = form_model_dict[category]['model_class']

    if topic_name == 'Integral' and category == "Functions":
        show_equation2 = (topic_name == 'Integral')
        form = form_class(show_equation2=show_equation2)
    elif (topic_name == 'Lagrange Polynomial' or topic_name == 'Fourier Transform') and category == "Functions":
        show_input = (topic_name == 'Lagrange Polynomial' or topic_name == 'Fourier Transform')
        form = form_class(show_input=show_input)
    elif category == "Functions":
        show_fields = (topic_name == 'Chebyshev Iteration' or topic_name == 'Simpson\'s Rule' 
                       or topic_name == 'Backward Difference Method'
                       or topic_name == 'Boole\'s Rule' or topic_name == 'Riemann Sum' or topic_name == 'Left Endpoint Rule'
                       or topic_name == 'Trapezoidal Rule')
        form = form_class(show_fields=show_fields)
    else:
        form = form_class()

    if request.method == 'POST':
        if topic_name == 'Integral' and category == "Functions":
            show_equation2 = (topic_name == 'Integral')
            form = form_class(request.POST,show_equation2=show_equation2)
        elif (topic_name == 'Lagrange Polynomial' or topic_name == 'Fourier Transform') and category == "Functions":
            show_input = (topic_name == 'Lagrange Polynomial' or topic_name == 'Fourier Transform')
            form = form_class(request.POST,show_input=show_input)
        elif category == "Functions":
            show_fields = (topic_name == 'Chebyshev Iteration' or topic_name == 'Simpson\'s Rule' 
                           or topic_name == 'Backward Difference Method'
                           or topic_name == 'Boole\'s Rule' or topic_name == 'Riemann Sum' or topic_name == 'Left Endpoint Rule'
                           or topic_name == 'Trapezoidal Rule')
            form = form_class(request.POST,show_fields=show_fields,)
        else:
            form = form_class(request.POST)

        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.user = request.user
            model_instance.topic = topic
            model_instance.category = topic.category
            model_instance.save()

        video_quality = "-qh"
        script_path = "MANIMath_Data/animations.py"
        command = f'manim {video_quality} {script_path} {topic.animation_class}'
        try:
            subprocess.run(command, check=True)
            video_path = f"../../static/media/manim/videos/animations/1080p60/{topic.animation_class}.mp4"
            video_html = render_to_string('partials/_video_section.html', {'video_path': video_path})
            return JsonResponse({'video_html': video_html})

        except subprocess.CalledProcessError as e:
            print(e)
            # Return error page

    return render(request, 'MANIMath_WebUI/create_animation.html', {'title' : topic_name, 'topic': topic, 'form': form})
