from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('my_test_http_response', views.my_test_http_response),
    path('my_test', views.my_test),
]