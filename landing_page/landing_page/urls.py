from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update-text', views.update_text, name='update'),
]