from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('register/', views.register_view, name='register'),
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
path('profile/<str:username>/', views.profile, name='profile'),
path('create/', views.create_post, name='create_post'),
path('post/<int:pk>/', views.post_detail, name='post_detail'),
path('delete/<int:pk>/', views.delete_post, name='delete_post'),
path('like/<int:pk>/', views.like_post, name='like_post'),
path('comment/edit/<int:pk>/', views.edit_comment, name='edit_comment'),
path('comment/delete/<int:pk>/', views.delete_comment, name='delete_comment'),
path('follow/<str:username>/', views.follow_user, name='follow_user'),
path('edit-profile/', views.edit_profile, name='edit_profile'),
]