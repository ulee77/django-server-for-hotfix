# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.
# class User(AbstractUser):
#     human_name = models.TextField("真实姓名", null=True, blank=True)
#     gpg_keyid = models.CharField(max_length=64, null=True, blank=True)
#     ssh_key = models.TextField(null=True, blank=True)
#     level = models.IntegerField('用例等级', choices=((1, '低'), (2, '中'), (3, '高')))
#
#     old_password = models.CharField("旧密码", max_length=127, null=True, blank=True)
#     password_changed = models.DateTimeField("修改密码的时间", auto_now_add=True)
#     passwordtoken = models.TextField("找回密码Token", null=True, blank=True)
#     passwordtoken_expires = models.DateTimeField("找回密码Token有效期限", null=True, blank=True)


class Case(models.Model):
    # suites = models.ManyToManyField(Suite)
    name = models.CharField("用例名称", max_length=255, unique=True)
    description = models.TextField('用例描述', blank=True, null=True)
    level = models.IntegerField('用例等级', choices=((1, '低'), (2, '中'), (3, '高')))
    command = models.TextField('命令', max_length=255, null=True)
    script = models.TextField('脚本', max_length=255, null=True)
    param = models.TextField('参数', max_length=255, null=True)
    createdAt = models.DateTimeField("创建的时间")
    modifyAt = models.DateTimeField("修改的时间", auto_now_add=True)

    def __str__(self):
        return self.name

class Suite(models.Model):
    #user = models.ForeignKey(User)
    name = models.CharField('套件名称', max_length=255, unique=True)
    description = models.TextField('套件描述', blank=True, null=True)
    createdAt = models.DateTimeField("创建的时间")
    modifyAt = models.DateTimeField("修改的时间", auto_now_add=True)
    cases = models.ManyToManyField(Case, blank=True, null=True)
    suites = models.ManyToManyField('self', blank=True, null=True, symmetrical=False)

    def __str__(self):
        return self.name

class Task(models.Model):
    #user = models.ForeignKey(User)
    suite = models.ForeignKey(Suite)
    name = models.CharField("任务名称", max_length=255, unique=True)
    description = models.TextField('任务描述', blank=True, null=True)
    createdAt = models.DateTimeField("创建的时间")
    modifyAt = models.DateTimeField("修改的时间", auto_now_add=True)

    def __unicode__(self):
        return self.name

class Task_Case(models.Model):
    case = models.ForeignKey(Case)
    task = models.ForeignKey(Suite)
    createdAt = models.DateTimeField("创建的时间", auto_now_add=True)

class Machine(models.Model):
    # suite = models.ForeignKey(Suite)
    name = models.CharField("主机名称", max_length=255, unique=True)
    description = models.TextField('主机描述', blank=True, null=True)
    address = models.IPAddressField('IP')
    status = models.IntegerField('主机状态', choices=((1, '在线'), (2, '离线')), default=2)
    createdAt = models.DateTimeField("创建的时间")
    modifyAt = models.DateTimeField("修改的时间", auto_now_add=True)

class Task_Report(models.Model):
    task = models.ForeignKey(Suite)
    machine = models.ForeignKey(Machine)
    result = models.IntegerField('结果', choices=((1, 'pass'), (2, 'fail'), (3, 'running'), (4, 'finish')), default=3)
    createdAt = models.DateTimeField("创建的时间", auto_now_add=True)
    #completedAt = models.DateTimeField("完成的时间", blank=True, null=True)

class Case_Report(models.Model):
    task_report = models.ForeignKey(Task_Report)
    case = models.ForeignKey(Case)
    result = models.IntegerField('结果', choices=((1, 'pass'), (2, 'fail'), (3, 'running'), (4, 'finish')), default=3)