from django.urls import path
from .views import LoginTemplateView,RegisterTemplateView,about
urlpatterns = [
    path('',about,name='about'),
    path('login/',LoginTemplateView.as_view(),name='login'),
    path('register/',RegisterTemplateView.as_view(),name='register'),
]