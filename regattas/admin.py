from django.contrib import admin
from .models import Club
from .models import Regatta

#registering my models
admin.site.register(Club)
admin.site.register(Regatta)
