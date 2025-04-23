"""
URL configuration for django_tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from .views import home_view

from recipes.views import (
    recipe_search_view,
    recipe_create_view,
    recipe_detail_view,
    recipe_update_view
)
from accounts.views import (
    login_view,
    logout_view,
    register_view
)



urlpatterns = [
    path('', home_view),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('recipes/', recipe_search_view),
    path('recipes/create/', recipe_create_view),
    path('recipes/<slug:slug>/', recipe_detail_view),
    path('recipes/<slug:slug>/update', recipe_update_view, name='update'),
    path('admin/', admin.site.urls),
]
