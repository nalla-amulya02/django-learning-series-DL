

from django.urls import path

from accounts.views import dashboard, home,register


urlpatterns = [
    path('',home),  #-> show the signup and login option only
    path('register/',register,name='register'),
    path('dashboard/',dashboard,name='dashboard'),
]



# localhost - see the page. to show options for register(signup) and login
