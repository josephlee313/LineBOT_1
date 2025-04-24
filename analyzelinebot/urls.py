from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('callback/', views.callback, name='callback'),
    path('health/', views.health_check, name='health_check'),
    path('test/', views.test, name='test'),
]
