from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/auth/', include('accounts.urls')),
    path('events/', include('events.urls', namespace='app_events')),
    # path("api/", include("api.urls")),
]