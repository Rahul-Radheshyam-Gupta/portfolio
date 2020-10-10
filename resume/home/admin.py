from django.contrib import admin

# Register your models here.
from .models import Project,Visitor



admin.site.register(Visitor)
admin.site.register(Project)
