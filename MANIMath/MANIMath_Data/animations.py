from manim import *
from sympy import *
from manim.utils.color import Color 
import requests
import random

####################################  Api Call ####################################

def api_call():
    base_url = 'http://localhost:61000/api/models/'
    url = f'{base_url}'
    headers = {'Authorization': 'Token c345e2d3135f5ceb80374d5fe6cbff13d9dbbb7a'}
    try:
        response = requests.get(url, headers=headers) 
        data = response.json()
        return data
    except requests.exceptions.HTTPError as e:
        print('HTTP Error:', e.response.status_code)
        return None


#################################### Manim Config ####################################

config.media_dir = r"MANIMath_WebUI/static/media/manim"
config.background_color = WHITE
config.background_opacity = 1

#################################### Animations ####################################

