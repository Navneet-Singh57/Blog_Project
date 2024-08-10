from django.urls import path
from .import views

urlpatterns = [
    path('main/', views.main, name="blog-main" ),
    path('', views.index, name="blog-index" ),
    path('about/', views.about, name="blog-about"),
    path('post_detail/<int:pk>',views.post_detail, name='blog-post-detail'),
    path('post_edit/<int:pk>',views.post_edit, name='blog-post-edit'),
    path('post_delete/<int:pk>',views.post_delete, name='blog-post-delete'),
]