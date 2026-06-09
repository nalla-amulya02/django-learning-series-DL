

from django.urls import path

from accounts import views
from accounts.views import dashboard, home,register


urlpatterns = [
    path('',home),  #-> show the signup and login option only
    path('register/',register,name='register'),
    path('dashboard/',dashboard,name='dashboard'),

    path(
        'students/',
        views.student_list,
        name='students'
    ),

    path(
        'add/',
        views.add_student,
        name='add'
    ),

    path(
        'edit/<int:id>/',
        views.edit_student,
        name='edit'
    ),

    path(
        'delete/<int:id>/',
        views.delete_student,
        name='delete'
    ),
]



# localhost - see the page. to show options for register(signup) and login
