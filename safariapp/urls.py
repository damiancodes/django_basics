from django.urls import path
from safariapp import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contact, name='contactus'),

    path('service/', views.service, name='service'),
]