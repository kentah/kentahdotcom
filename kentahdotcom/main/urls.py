from django.urls import path

from main import views


urlpatterns = [
    path('', views.Main.as_view(), name='main'),
]