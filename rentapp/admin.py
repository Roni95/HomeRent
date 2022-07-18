from django.contrib import admin

# Register your models here.
from .models import *

#from django.contrib.admin.models import LogEntry
#LogEntry.objects.all().delete()

admin.site.site_header = "RentHome"
admin.site.site_title = "RentHome"


# Register your models here.
admin.site.register(RentPost)
