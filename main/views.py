# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import json

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

from django.http import  HttpResponse

def ajax_data(request):
    data = {'a':5,'b':10,'c':15}
    dump = json.dumps(data)
    return HttpResponse(dump)