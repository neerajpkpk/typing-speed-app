from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import setup_view
urlpatterns = [
    path('', views.home_view, name='home'),

    path('custom-text/', views.custom_text_view, name='custom_text'),
    path('default-text/', views.default_text_view, name='default_text'),

    # SEO/verification/static plain text files
    path("robots.txt", TemplateView.as_view(template_name="testapp/robots.txt", content_type="text/plain")),
    path("googlec47f5d51e638c428.html", TemplateView.as_view(template_name="googlec47f5d51e638c428.html", content_type="text/html")),
    path('setup/',setup_view),
    
    
]

