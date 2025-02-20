from django.urls import path
from safariapp import views
urlpatterns = [
    path('', views.index, name='my_index'),
    path('about/', views.about, name='my_about'),

    path('service/', views.service, name='my_service'),
]