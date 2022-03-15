import imp
from tkinter.tix import Tree
from unittest import result
from urllib import request
from django.http import JsonResponse
from django.shortcuts import render
from .models import Apps,Screenshots
from django.db.models import Max
import random

def get_random(exclude):
    max_id = Apps.objects.all().aggregate(max_id = Max("id"))['max_id']
    while True:
        pk = random.randint(1,max_id)
        print(type(pk))
        print(type(exclude))
        print(pk != int(exclude))
        if pk != int(exclude) :
            screenshots = Screenshots.objects.filter(app_id = pk)
            if screenshots:
                return screenshots, pk
    

# Create your views here.
def random_match(response):
    ls = Apps.objects.all()
    lsc = Apps.objects.get(id=1)
    return render(response,"apps_screenshots/random_match.html", {"ls":ls})

def get_screenshot(response):
    if response.method == 'POST':
        app_name = response.POST.get('app_name')
        screenshots = Screenshots.objects.filter(app_id = app_name)
        print(app_name)
        if not screenshots.exists():
            return JsonResponse({'status':'error'})
    
    return JsonResponse({'screenshots': list(screenshots.values())})

def get_random_screenshots(response):
    previous_app = response.POST.get('previous_app')
    result = get_random(previous_app)
    selected_screenshots = result[0]
    current_app = result[1]

    resp = JsonResponse({'randomscreenshots': list(selected_screenshots.values()), 'current_app': current_app})

    return resp
