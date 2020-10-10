from django.urls import path
from .views import dashboard,about,contact,project
app_name = 'home'
urlpatterns = [
    path('',dashboard,name='dashboard' ),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact' ),
    path('project/',project,name='project' ),
]
