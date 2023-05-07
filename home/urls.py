from django.urls import path, include
from .views import home,projectname1,projectname2,projectform1

app_name = 'home'

urlpatterns = [
    path('',home,name='home1'),
    path('projectname1',projectname1,name='projectname1'),
    path('projectname2',projectname2,name='projectname2'),
    path('project1form',projectform1,name='projectform1')
]
