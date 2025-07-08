"""
URL configuration for typing_project project.

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
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from testapp.sitemaps import StaticViewSitemap
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
import os



sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns = [
    path('neeraj-site/', admin.site.urls),
    path('', include('testapp.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),  # ✅ Ye line add karo
      path('googlec47f5d51e638c428.html', serve, {
        'path': 'googlec47f5d51e638c428.html',
        'document_root': os.path.join(settings.BASE_DIR, 'static'),
    }),
]


