#encoding:utf-8
from django.db import models
from django import forms
class Person(models.Model):
    name = models.CharField('姓名',max_length=30)
    age = models.IntegerField('年龄')
    def __unicode__(self):
        return 'name:%s|age:%s'%(self.name,self.age)
    class Meta:
        verbose_name="员工姓名"
        verbose_name_plural="员工信息"
class Account(models.Model):
    username = models.CharField('用户名',max_length=10)
    password = models.CharField('密码',max_length=20)
    email = models.EmailField('邮箱',)
    phone = models.CharField('手机号',max_length=11)
    def __unicode__(self):
        return 'username:%s\npassword:%s\nemail:%s\nphone:%s'%(self.username,self.password,self.email,self.phone)
