from django.urls import path
from app2.views import *
app_name='something2'
urlpatterns=[
    path('bujji/',bujji,name='bujji'),
    path('sowmya/',sowmya,name='sowmya'),
]