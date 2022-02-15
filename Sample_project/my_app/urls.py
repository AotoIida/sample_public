from django.urls import path
from . import views

app_name = 'my_app'


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('list/', views.list, name='list'),
    path('regist/', views.regist, name='regist'),

    path('page/<str:user_name>', views.user_page, name='user_page'),
]