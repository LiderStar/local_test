from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views
from .views import BookViewSet

router = SimpleRouter()
router.register(r'booki', BookViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("view/", views.view, name="view"),
]

urlpatterns += router.urls
