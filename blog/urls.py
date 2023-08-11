"""This module holds url paths used in blog app."""

from . import views
from django.urls import path


urlpatterns = [ 
  path('', views.PostList.as_view(), name='home'),
  path('detail/<slug:slug>/', views.PostDetail.as_view(), name='detail_page')
]
