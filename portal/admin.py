from django.contrib import admin
from . models import Job, Blog, Chat, Test

# Register your models here.
admin.site.register(Job)
admin.site.register(Blog)
admin.site.register(Chat)
admin.site.register(Test)