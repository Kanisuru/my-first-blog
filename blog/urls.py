from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='postNew'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]