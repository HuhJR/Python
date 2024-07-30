# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:28:06 2024

@author: KITCOOP
"""

from django.urls import path
from . import views

urlpatterns = [
    path("write/", views.write, name="write"),
    path("list/", views.list1, name="list"), 
    path("info/<int:num>", views.info, name="info"),
    path("update/<int:num>", views.update, name="update"),
    path("delete/<int:num>", views.delete, name="delete"),
    path("restlist", views.restlist1, name="list"),
    path("commentpro/<str:comment>/<int:num>", views.commentpro, name="commentpro"),
]