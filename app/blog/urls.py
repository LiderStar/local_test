from django.urls import path
from blog.views import UserPostListView

from blog import views

urlpatterns = [
    path("posts/user/<str:username>/", UserPostListView.as_view(), name="user_posts_list"),

]
