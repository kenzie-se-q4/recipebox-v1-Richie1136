"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import login
from django.urls import path

from recipe_app import views

urlpatterns = [
    path('recipe/<int:recipe_id>/', views.recipe_detail, name="recipe_detail"),
    path('author/<int:author_id>/', views.author_detail),
    path('addrecipe/', views.add_recipe),
    path('addauthor/', views.add_author),
    path('', views.index, name='homepage'),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('recipe/<int:recipe_id>/edit/', views.edit_recipe, name='edit'),
    path('recipe/<int:recipe_id>/favorite/',
         views.favorite_this_recipe, name='favorite'),
]
