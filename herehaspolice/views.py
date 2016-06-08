from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.utils.translation import ugettext_lazy as _
import logging
import datetime
from datetime import date
import operator
import json
from django.core.handlers.wsgi import logger
from herehaspolice.models import *
from django.db import connection
from django.contrib import messages
from django.db.models import Max
from herehaspolice.forms import Error_ReportForm

def home(request):
    args = []
    path = 'herehaspolice/base.html'
    
    if request.method == 'POST':
        logger.debug("insert latlon information into DB")
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        text = request.POST.get('text')

        if lat and lon:
            #get ip address
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ipaddress = x_forwarded_for.split(',')[-1].strip()
            else:
                ipaddress = request.META.get('REMOTE_ADDR')
            
            record = GeoInfo.objects.filter(ipaddress=ipaddress).aggregate(Max('datetime_added'))
            today = datetime.datetime.now()
            
            if record['datetime_added__max'] is None:
                GeoInfo.objects.create(lat=lat, lon=lon, text=text, ipaddress=ipaddress)
                messages.success(request, _('thanks for your sharing'))
            else:
                if (today-record['datetime_added__max']).total_seconds() > 10:
                    GeoInfo.objects.create(lat=lat, lon=lon, text=text, ipaddress=ipaddress)
                    messages.success(request, _('thanks for your sharing'))
                else:
                    messages.error(request, _('report too soon to response, please wait 10secs'))
        else:
            messages.error(request, _('No GPS Info'))
            
    #fetch all records within 1 day
    base_sql = "SELECT lat, lon, TIME_FORMAT(TIMEDIFF(NOW(), datetime_added), '%H:%i') FROM herehaspolice_geoinfo WHERE datetime_added > now() - INTERVAL 1 DAY;"
    curs = connection.cursor()
    curs.execute(base_sql)
    results = json.dumps(curs.fetchall())
    
    args = {'title' : 'Police Here!!',
            'locs_json' : results,
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
    
    
def about(request):
    args = {'title' : 'Police Here!!'}
    
    return render_to_response(
        'herehaspolice/_about.html',
        args,
        context_instance=RequestContext(request)
    )
    
    
    
def error_report(request):
    
    if request.method == 'POST':
        error_reportform = Error_ReportForm(request.POST)
        
        #get ip address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')
        
        if error_reportform.is_valid():
            errorContent = error_reportform.cleaned_data['errorContent']
            ErrorReport.objects.create(errorContent=errorContent, 
                                       ipaddress=ipaddress)
            
    
    error_reportform = Error_ReportForm()
    #get all info from db
    errorReports = ErrorReport.objects.all().order_by('-reportDT')
    
    args = {'title' : 'Police Here!!',
            'error_reportform' : error_reportform,
            'errorReports' : errorReports,
            }
    
    return render_to_response(
        'herehaspolice/_error_report.html',
        args,
        context_instance=RequestContext(request)
    )