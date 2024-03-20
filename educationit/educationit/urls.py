"""
URL configuration for educationit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from graphene_django.views import GraphQLView
from Users.views import ContactView, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/signup/', RegisterView.as_view(), name='auth_signup'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('api.urls')),
    path('course/', include('Courses.urls')),
    path('contact/', ContactView.as_view(), name='contact'),
    path("__debug__/", include("debug_toolbar.urls")),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]
