from django.urls import path
from . import views
# '.' 현재 위치(폴더)

# url 변수화
app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
]