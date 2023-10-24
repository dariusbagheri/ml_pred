# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='index_old'),
    # path('', views.index_four, name='index'),
    # path('', views.login, name='pages'),
    path("chat/financials/", views.chat_window, name="room"),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
