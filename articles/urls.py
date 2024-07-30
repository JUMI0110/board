from django.urls import path
from . import views
# '.' 현재 위치(폴더)

urlpatterns = [
    path('', views.index),
]