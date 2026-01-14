"""
URL configuration for finance_tracker project.

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
from django.urls import path, include

from django.views.generic.base import RedirectView
from django.conf import settings

from django.contrib.sitemaps.views import sitemap
from blog.sitemap import BlogSitemap
from finance_tracker.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', RedirectView.as_view(pattern_name='account_login', permanent=True)), # Redirect legacy login
    path('accounts/', include('allauth.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('favicon.ico', RedirectView.as_view(url='/static/img/pwa-icon-512.png')),
    path('apple-touch-icon.png', RedirectView.as_view(url='/static/img/pwa-icon-512.png')),
    path('apple-touch-icon-precomposed.png', RedirectView.as_view(url='/static/img/pwa-icon-512.png')),
    path('blog/', include('blog.urls')),
    path('', include('expenses.urls')),
]
