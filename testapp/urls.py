from django.urls import path
from  . import views
from django.views.generic import TemplateView
urlpatterns=[
    path('',views.home_view,name='home'),
   
     path('custom-text/', views.custom_text_view, name='custom_text'),
     path("robots.txt", TemplateView.as_view(template_name="testapp/robots.txt", content_type="text/plain")),
     path('default-text/', views.default_text_view, name='default_text'), 
     path('googlec47f5d51e638c428.html', TemplateView.as_view(template_name="googlec47f5d51e638c428.html")),
     path('setup/', setup_view),





]


