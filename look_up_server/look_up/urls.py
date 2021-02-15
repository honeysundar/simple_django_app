from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('count', views.welcome, name='welcome'),
    path('<str:server_id>/', views.server, name="server"),
]