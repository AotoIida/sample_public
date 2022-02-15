from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.forms import UserForm, ProfileForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import Profile #モデルからDBデータをひきだすため

from django.contrib.auth.models import User #外部キーからデータを引き出したいからインポート？

from django.urls import reverse
from urllib.parse import urlencode

# Create your views here.

def user_list(request): #02/10 12:41 今profileだけインポートしてるけど、合体した方がいいかも
    profile = Profile.objects.all() #全件取得
    return render(request, 'user/user_list.html', context={
        'profile' : profile
    })


def index(request):
    profile = Profile.objects.all() #全件取得
    return render(request, 'user/index.html', context={
        'profile' : profile
    })

def register(request):
    user_form = UserForm(request.POST or None) 
    profile_form = ProfileForm(request.POST or None, request.FILES or None)
    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save() #ModelFormのsaveメソッドを実行してユーザー登録
        user.set_password(user.password) #ユーザのレコードにパスワードを保存できる
        user.save() #ユーザーを保存

        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
    return render(request, 'user/register.html', context={
        'user_form': user_form,
        'profile_form': profile_form,
    })

def user_login(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        #上記まででユーザー情報とパスワードをホームから取得することができた.
        #次はそれが正しいか（ユーザーが存在して、そのパスワードが正しいかどうかを判定）
        #Djangoではそれがデフォルトで用意されているので、インポートする（authenticate,login）
        #あとついでに、redirectとHttpResponceもインポート
        user = authenticate(username=username, password=password)

        if user: #ユーザが存在する場合
            if user.is_active: #さらにユーザが有効な場合は
                login(request, user) #ログインする
#                URL = reverse('user:index')
#                parameter = urlencode({'NAME' : username}) #49~51　おためし
#                plusURL = f'{URL}?{parameter}'
#                return redirect(plusURL)
#                return redirect('user:index', NAME=1)
                return render(request, 'user/index.html', context={
                    'username' : username
                })

            else:
                return HttpResponse('アカウントが有効ではありません')
        else:
            return HttpResponse('ユーザが存在しません')
    return render(request, 'user/login.html', context={
        'login_form': login_form
    })

@login_required
def user_logout(request):
    logout(request) #これだけでログアウト処理実装（インポートする必要ある）
    return redirect('user:index')

#ログアウト処理まで実装出来たら次はLoginrequiredを設定（ログインしていないと関数を実行できないように）

@login_required
def info(request):
    return HttpResponse('すでにログインしています')