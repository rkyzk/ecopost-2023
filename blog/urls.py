"""This module holds url paths used in blog app."""

from . import views
from django.urls import path


urlpatterns = [ 
  path('', views.PostList.as_view(), name='home'),
  path('add_story/', views.AddStory.as_view(), name='add_story'),
  path('detail/<slug:slug>/', views.PostDetail.as_view(), name='detail_page')
]
