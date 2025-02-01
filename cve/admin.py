from django.contrib import admin
from .models import Cve

# Register your models here.
# This allows the object to be created and modified in the admin portal.
admin.site.register(Cve)