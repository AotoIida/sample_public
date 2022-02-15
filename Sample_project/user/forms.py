from django import forms
from django.contrib.auth.models import User
from user.models import Profile


class UserForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
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


class ProfileForm(forms.ModelForm):
    fruits = forms.CharField(label='果物')
    website = forms.URLField(label='ホームページ')
    picture = forms.FileField(label='写真')

    class Meta:
        model = Profile
        fields = ('fruits', 'website', 'picture')


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
