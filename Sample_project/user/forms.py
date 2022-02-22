from django import forms
from django.contrib.auth.models import User
from user.models import Profile


class UserForm(forms.ModelForm): #デフォルトのログイン機能のテーブル
    username = forms.CharField(label='ニックネーム　　')
    email = forms.EmailField(label='メールアドレス　')
    password = forms.CharField(label='パスワード　　　', widget=forms.PasswordInput())
    Cpassword = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        Cpassword = cleaned_data['Cpassword']
        if password != Cpassword:
             raise forms.ValidationError('パスワードが一致しません')


class ProfileForm(forms.ModelForm): #自作のプロフィテーブル
    fruits = forms.CharField(label='くだもの　　', required=False)
    age = forms.IntegerField(label='年齢　　　　',required=False)
    hobby = forms.CharField(label='趣味　　　　',required=False)
    website = forms.URLField(label='ホームページ', required=False)
    picture = forms.FileField(label='アイコン画像', required=False, initial="user/nosettings.png")

    class Meta:
        model = Profile
        fields = ('fruits', 'age', 'hobby', 'website', 'picture')


class LoginForm(forms.Form):
    username = forms.CharField(label='ユーザー名', max_length=30)
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
             raise forms.ValidationError('パスワードが一致しません')
