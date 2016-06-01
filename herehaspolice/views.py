from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
import logging
import datetime
import operator
import json
import re
from django.core.handlers.wsgi import logger
from herehaspolice.models import *




def home(request):
    args = []
    path = 'herehaspolice/base.html'
    
    if request.method == 'POST':
        logger.debug("insert latlon information into DB")
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        text = request.POST.get('text')
        logger.debug("lat=%s" % lat)
        logger.debug("lon=%s" % lon)
        logger.debug("text=%s" % text)
        
        GeoInfo.objects.create(lat=lat, lon=lon, text=text)
        
        args = {'title' : 'Police Here!!',
                }
        
        
    elif request.method == 'GET': #display main page
        
        args = {'title' : 'Police Here!!',
                }
    
    return render_to_response(
        path,
        args,
        context_instance=RequestContext(request)
    )