from django.urls import path
from safariapp import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('', views.contact, name='contact'),
]