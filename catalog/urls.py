"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin,auth
from django.urls import path,include
from django.views.generic.base import RedirectView
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    
	path('', views.index,name='index'),
    path('books/', views.BookListView.as_view(),name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(),name='book-details'),
    path('authors', views.AuthorListView.as_view(),name='authors'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(),name='author-details'),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    path('accounts/logout', auth_views.LogoutView.as_view(template_name='registration/logged_out.html')),
]