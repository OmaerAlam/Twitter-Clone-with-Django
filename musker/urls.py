from django.urls import path
from . import views

urlpatterns = [
    # Home page - Meep feed
    path('', views.home, name="home"),
    # List of all profiles except current user
    path('profile_list/', views.profile_list, name='profile_list'),
    # Individual user profile view
    path('profile/<int:pk>', views.profile, name='profile'),
    # View user's followers
    path('profile/<int:pk>/followers/', views.followers, name='followers'),
    # View who the user is following
    path('profile/<int:pk>/follows/', views.follows, name='follows'),
    # Login page
    path('login/', views.login_user, name='login'),
    # Logout user
    path('logout', views.logout_user, name='logout'),
    # User registration page
    path('register/', views.register_user, name='register'),
    # Update user and profile info
    path('update_user/', views.update_user, name='update_user'),
    # Like or unlike a meep
    path('meep_like/<int:pk>', views.meep_like, name="meep_like"),
    # View a specific meep
    path('meep_show/<int:pk>', views.meep_show, name="meep_show"),
    # Unfollow a user
    path('unfollow/<int:pk>', views.unfollow, name="unfollow"),
    # Follow a user
    path('follow/<int:pk>', views.follow, name="follow"),
    # Delete a meep
    path('delete_meep/<int:pk>', views.delete_meep, name="delete_meep"),
    # Edit a meep
    path('edit_meep/<int:pk>', views.edit_meep, name="edit_meep"),
    # Search meeps
    path('search/', views.search, name='search'),
]
