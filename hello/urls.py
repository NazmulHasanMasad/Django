from django.urls import path

from .import views 
urlpatterns=[
    path("", views.index, name="index"),
    path("Masad", views.Masad, name="brain"),
    path("<str:name>", views.greet, name="greet") 
 ]    
