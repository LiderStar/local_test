from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from app import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("store/", include('store.urls')),
    path("", include('blog.urls')),
    path('accounts/', include('allauth.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    # path('__debug__/', include('debug_toolbar.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)