
from django.contrib import admin
from django.urls import include, path

# urls
urlpatterns = [
    path('api/v1/students/', include('students.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
]