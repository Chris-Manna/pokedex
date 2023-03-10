  
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("following", views.following, name="following"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    # path("post", views.new_post, name="new_post"),
    # path("posts/<int:post_id>", views.post, name="post"),
    # path("posts/<int:post_id>/edit", views.edit, name="edit"),
    # path("monster", views.new_monster, name="new_monster"),
    # path("monsters/<int:monster_id>", views.monster, name="single_monster"),
    path("monster/csv", views.monster_csv, name="monster_csv"),
    path("register", views.register, name="register"),
    path("users/<str:username>", views.user, name="user"),
    path("users/<str:username>/follow", views.follow, name="follow"),
    path("users/<str:username>/unfollow", views.unfollow, name="unfollow")
]