from django.urls import path
from blog.views import UserPostListView, AllPostListView

from blog import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("posts/user/<str:username>/", UserPostListView.as_view(), name="user_posts_list"),
    path("posts/all/", AllPostListView.as_view(), name="all_posts_list"),
    path("posts/add/", views.add_post, name="add_post"),
    path("posts/addform/", views.add_post2, name="add_post_model"),

]
