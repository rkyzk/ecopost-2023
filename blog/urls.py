"""This module holds url paths used in blog app."""

from . import views
from django.urls import path


urlpatterns = [ 
  path('', views.PostList.as_view(), name='home'),
  path('add_story/', views.AddStory.as_view(), name='add_story'),
  path('update/<slug:slug>/', views.UpdatePost.as_view(),
       name='update_post'),
  path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
  path('bookmark/<slug:slug>/', views.Bookmark.as_view(),
       name='bookmark'),
  path('detail/<slug:slug>/', views.PostDetail.as_view(), name='detail_page')
]
