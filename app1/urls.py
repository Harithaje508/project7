from app1.views import *
from django.urls import path
app_name='DayDreamer'
urlpatterns=[
    path('sanem/',sanem,name='sanem'),
]