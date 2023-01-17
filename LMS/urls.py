from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ManagementEntities/', include('ManagementEntities.urls')),
    path('admin/', admin.site.urls),
]