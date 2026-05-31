from django.urls import path

from review import views


urlpatterns = [
    path('', views.index, name='index'),
    path('thank-you',views.thanks),
]
