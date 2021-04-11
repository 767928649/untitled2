from django.db import models

# Create your models here.


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField('用户名称', max_length=50)
    phone = models.CharField('用户电话', max_length=50)
    age = models.CharField('年龄', max_length=50)
    created = models.DateTimeField('提交时间', auto_now_add=True)