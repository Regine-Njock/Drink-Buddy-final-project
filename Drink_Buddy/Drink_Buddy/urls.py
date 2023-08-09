"""
URL configuration for Drink_Buddy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from drink_service import views
from django.conf.urls.static import static
from django.conf import settings
from users import views as user_views
from rest_framework import routers
from Educational.api_views import EducationalViewSet, EducationalListAPIView, EducationalDetailAPIView, EducationalCreateAPIView, EducationalUpdateAPIView,EducationalDeleteAPIView
router = routers.DefaultRouter()
router.register('edu',EducationalViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name='home'),
    path("register/", user_views.register, name='register'),
    path("profile/", user_views.profile, name='profile'),
    path("login/", auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path("landing/", views.landing_page, name='landing_page'),
    path('response/', views.response_page, name= 'response_page'),
    path('premium/', views.premium, name= 'premium'),
    path("", include('drink_service.urls')),
    path("", include('blog.urls')),
    path('Educational/', include('Educational.urls')),
    path('edu_list/', include(router.urls)),
    path('api/v1/', EducationalListAPIView.as_view(), name='api-list-educational'),
    path('api/v1/create', EducationalCreateAPIView.as_view(), name='api-create-educational'),
    path('api/v1/<int:pk>', EducationalDetailAPIView.as_view(), name='api-detail-educational'),
    path('api/v1/update/<int:pk>', EducationalUpdateAPIView.as_view(), name='api-update-educational'),
    path('api/v1/delete/<int:pk>', EducationalDeleteAPIView.as_view(), name='api-delete-educational'),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
