from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('leads.url')),
    path('admin/', admin.site.urls),
]
