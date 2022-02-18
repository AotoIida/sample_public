from django.urls import path
from . import views

app_name = 'user'


urlpatterns = [ #viewの名前かも
    path('user_list/', views.user_list, name ='user_list'),
    path('index/', views.index, name ='index'),
    path('register/', views.register, name ='register'),
    path('user_login/', views.user_login, name ='user_login'),
    path('user_logout/', views.user_logout, name ='user_logout'),
    path('info/', views.info, name ='info'),
    path('', views.first, name ='first'), #自動遷移用・・・本当にやり方あっているのかわからない
]