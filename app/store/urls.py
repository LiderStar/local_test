from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views
from .views import BookViewSet, BookListView, AuthorListView

router = SimpleRouter()
router.register(r'booki', BookViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("view/", views.view, name="view"),
    path("view/book/", BookListView.as_view(), name="book_list"),
    path("book/<str:author>/", AuthorListView.as_view(), name="author_list"),
]

urlpatterns += router.urls
