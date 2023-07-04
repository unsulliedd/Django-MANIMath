import subprocess,os,re
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, JsonResponse
from django.template.loader import render_to_string
from datetime import datetime
from django.db.models import Q
from .models import *
from .forms import *
from MANIMath_Data.animations import animations
from rest_framework.authtoken.models import Token

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

    form = form_class()

    if request.method == 'POST':
        form = form_class(request.POST)

        if form.is_valid():
            model_class = form.save(commit=False)
            model_class.user = request.user
            model_class.topic = topic
            model_class.category = topic.category
            model_class.save()

        #try:
        #    token = Token.objects.get(user=request.user)
        #except Token.DoesNotExist:
        #    token = Token.objects.create(user=request.user)

        #token_str = str(token)
        #animations_file_path = os.path.join("MANIMath_Data/animations.py")
        #with open(animations_file_path, "r") as file:
        #    lines = file.readlines()

        #with open(animations_file_path, "w") as file:
        #    for line in lines:
        #        if "'Authorization': '" in line:
        #            header_value = re.search(r"'([^']*)'", line).group(1)
        #            line = line.replace(header_value, token_str)
        #        file.write(line)

        video_quality = "-qh"
        script_path = "MANIMath_Data/animations.py"
        command = f'manim {video_quality} {script_path} {topic.name}'
        try:
            subprocess.run(command, check=True)
            video_path = f"../../static/media/manim/videos/animations/1080p60/{topic.name}.mp4"
            video_html = render_to_string('partials/_video_section.html', {'video_path': video_path})
            return JsonResponse({'video_html': video_html})

        except subprocess.CalledProcessError as e:
            print(e)
            # Return error page

    return render(request, 'MANIMath_WebUI/create_animation.html', {'title' : topic_name, 'topic': topic, 'form': form})