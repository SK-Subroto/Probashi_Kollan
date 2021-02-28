from django.contrib import admin
from . models import Immigrant, Attendant, Country

# Register your models here.
admin.site.register(Immigrant)
admin.site.register(Attendant)
admin.site.register(Country)
