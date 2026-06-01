from django.urls import path

from review import views


urlpatterns = [
    # path('', views.index, name='index'),    #FBV
    path('', views.ReviewView.as_view(), name='index'),    #CBV
    path('thank-you', views.ThanksView.as_view()),
]
