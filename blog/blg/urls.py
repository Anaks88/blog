from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="blg_home"),
    path('about/',views.about,name="blg_abt")
]