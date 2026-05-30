from . import views
from django.urls import path
urlpatterns = [
    path("", views.hello ),    #hello/
    path("<str:name>/", views.hello_name)   #hello/any_name

    
]