from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name = 'blog_list'),
    path('blogs/create/', views.blog_create,name ='blog_create'),
    path('blogs/<int:id>/detail/', views.blog_details ,name='blog_details'),
    path('blogs/<int:id>/update/', views.blog_update ,name ='blog_update'),
    path('blogs/<int:id>/delete/', views.blog_delete ,name = 'blog_delete')
]