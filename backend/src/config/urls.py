"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from apps.accounts.api.auth_views import CustomTokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.accounts.api.urls')),
    path('api/v1/', include('apps.students.urls')),
    path('api/v1/auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/v1/", include("apps.announcements.urls")),
    path("api/v1/", include("apps.events.urls")),
    path("api/v1/", include("apps.clubs.urls")),
   path("api/v1/", include("apps.notifications.urls")),
]
