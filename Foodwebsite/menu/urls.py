from django.urls import path
from . import views
urlpatterns = [
    path('pizza/', views.pizza),    #/menu/pizza/
    path('<int:index>/', views.item_by_index),  #/menu/1
    path('<str:item>/', views.item_by_name),    #/menu/pizza/
    
]

# /menu/pizza/ - basic
# /menu/1 - dynamic




