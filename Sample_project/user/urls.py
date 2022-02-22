from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'user'


urlpatterns = [ #viewの名前かも
    path('user_list/', views.user_list, name ='user_list'),
    path('index/', views.index, name ='index'),
    path('register/', views.register, name ='register'),
    path('user_login/', views.user_login, name ='user_login'),
    path('user_logout/', views.user_logout, name ='user_logout'),
    path('info/', views.info, name ='info'),
    path('profile/', views.profile, name ='profile'),
    path('', views.first, name ='first'), #自動遷移用・・・本当にやり方あっているのかわからない
]

# これは通常DEBUGモードのみ付け加えるオプションで、本番はApache側で設定が必要！！
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
