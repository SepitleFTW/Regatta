from django.contrib import admin
from .models import Club
from .models import Regatta
from .models import Race

#registering my models
admin.site.register(Club)
admin.site.register(Regatta)
admin.site.register(Race)