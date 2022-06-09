from django.urls import path
from . import views

app_name = "compute"
urlpatterns = [
    path('', views.Home.as_view(), name='homepage'),
]