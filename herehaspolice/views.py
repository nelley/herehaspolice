from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
import logging
import datetime
from datetime import date
import operator
import json
import re
from django.core.handlers.wsgi import logger
from herehaspolice.models import *
from django.core.serializers.json import DjangoJSONEncoder


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
        
        today = date.today()
        locs = GeoInfo.objects.filter(datetime_added__contains=today).values_list('lat','lon', 'datetime_added')
        locs_json = json.dumps(list(locs), cls=DjangoJSONEncoder)
        
        args = {'title' : 'Police Here!!',
                'locs_json' : locs_json
                }
        
        
    elif request.method == 'GET': #display main page
        #get locations from DB
        today = date.today()
        locs = GeoInfo.objects.filter(datetime_added__contains=today).values_list('lat','lon', 'datetime_added')
        #locs = GeoInfo.objects.filter(datetime_added__contains=today).values_list('lat','lon')
        locs_json = json.dumps(list(locs), cls=DjangoJSONEncoder)
        
        args = {'title' : 'Police Here!!',
                'locs_json' : locs_json
                }
    
    return render_to_response(
        path,
        args,
        context_instance=RequestContext(request)
    )
    
def tmp(request):
    
    today = date.today()
    locs = GeoInfo.objects.filter(datetime_added__contains=today).values_list('lat','lon', 'datetime_added')
    #locs = GeoInfo.objects.filter(datetime_added__contains=today).values_list('lat','lon')
    locs_json = json.dumps(list(locs), cls=DjangoJSONEncoder)
        
    args = {'title' : 'Police Here!!',
            'locs_json' : locs_json}
    
    return render_to_response(
        'herehaspolice/tmp.html',
        args,
        context_instance=RequestContext(request)
    )