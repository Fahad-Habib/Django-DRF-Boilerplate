"""boilerplate URL Configuration."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('user/', include('users.urls')),
    path('api/user/', include('users.api.urls')),
]
