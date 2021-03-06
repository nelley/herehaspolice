from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class GeoInfo(models.Model):
    
    lat = models.FloatField(verbose_name=_('Latitude:'),
                                          help_text=_('Please input Latitude'))

    lon = models.FloatField(verbose_name=_('Longitude:'),
                                   help_text=_('Please input Longitude'))
    
    datetime_added = models.DateTimeField(null=False, default=timezone.now())
    
    text = models.CharField(max_length=40, 
                                verbose_name=_('Free command:'),
                                help_text=_('Please Input Free Command'))
