import random
import os
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # Added Kubernetes ConfigMap (Task6)
    hostname = os.environ['HOSTNAME']
    configmap_value1 = os.environ['LARGE_SYSTEMS_DJANGO_CONFIGMAP_value1']
    configmap_value2 = os.environ['LARGE_SYSTEMS_DJANGO_CONFIGMAP_value2']
    
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    myRandomNumber = a + b
    html = "<html><body style='background:black'><h1 style='color:lightgreen'>Random numbers addition: " + str(myRandomNumber) + "</h1><h2 style='color:magenta'>environ for HOSTNAME=" + hostname + "</h2><h2 style='color:cyan'>ConfigMap for LARGE_SYSTEMS_DJANGO_CONFIGMAP_value1=<color style='color:tomato'>" + configmap_value1 + "</color></h2><h2 style='color:cyan'>ConfigMap for LARGE_SYSTEMS_DJANGO_CONFIGMAP_value2=<color style='color:tomato'>" + configmap_value2 + "</color></h2><img src='https://e1.pxfuel.com/desktop-wallpaper/502/274/desktop-wallpaper-retro-gamer-gamer-kid.jpg' alt='Hacker wallpaper'></body></html>"
    return HttpResponse(html)