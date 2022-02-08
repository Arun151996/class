from django.urls import path
from . import views

urlpatterns=[
    path('note',views.Home),
    path('login',views.log,name="bike")
]
