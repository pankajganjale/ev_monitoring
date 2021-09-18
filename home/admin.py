from django.contrib import admin
# Register your models here.
from home.models import Contact, Measurement

admin.site.register(Contact)
admin.site.register(Measurement)
