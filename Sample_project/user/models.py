from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fruits = models.CharField(max_length=15, blank=True)
    #追加 20220222
    age = models.PositiveIntegerField(blank=True, default=0)
    hobby = models.CharField(max_length=15, blank=True)
    website = models.URLField(blank=True)
    picture = models.FileField(upload_to='user/' , blank=True) #mediaの設定が必要


    def __str__(self):
        return self.user.username