from . import views
from django.urls import path


urlpatterns = [

     path('', views.index, name='home'),

    path('contact/', views.contact, name='contact'),

     path('about/', views.about, name='about'),
    path('upload/', views.upload, name='upload'),
    path('logout/', views.logout1, name='logout'),
    path('footer/', views.footer, name='footer'),
    path('blogs/<int:blog_id>/', views.detail, name='detail'),


]