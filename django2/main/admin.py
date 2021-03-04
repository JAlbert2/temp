from django.contrib import admin
from .models import Patient, xapi, xapiRaw

# Register your models here.

admin.site.register(Patient)
admin.site.register(xapi)
admin.site.register(xapiRaw)