from django.contrib import admin

# Register your models here.
from .models import Project,Visitor,MyCv


admin.site.register(MyCv)
admin.site.register(Visitor)
admin.site.register(Project)
