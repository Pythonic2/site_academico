from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage.as_view(), name='home_page'),
    path('blog/',views.TestePage.as_view(), name='blog'),
]