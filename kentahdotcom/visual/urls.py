from django.urls import path

from visual import views


urlpatterns = [
    path('', views.Visual.as_view(), name='visual'),
]