from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('UserDetail', views.UserDetail.as_view(), name='UserDetail'),

]