"""
URL configuration for web project.

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
from API import views
from rest_framework import routers
from .yasg import urlpatterns as doc

router = routers.DefaultRouter()
router.register(r'api/serials', views.SerialsApi)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index_views.as_view()),
    path('', include(router.urls)),
    

]

urlpatterns+=doc