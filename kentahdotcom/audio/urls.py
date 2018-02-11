from django.urls import path

from audio import views


urlpatterns = [
    path('', views.Audio.as_view(), name='audio'),
]