# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:28:06 2024

@author: KITCOOP
"""

from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("join/", views.join, name="join"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("joinInfo/", views.info, name="info"),
    
    path("memberUpdate/", views.update, name="update"),
    path("memberDelete/", views.delete, name="delete"),
    path("passchg/<str:id>/", views.passchg, name="passchg"),
    path("picture/", views.picture, name="picture"),
    path("memberList/", views.list1, name="memberList"),
]