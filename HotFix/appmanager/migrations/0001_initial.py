# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='\u7528\u4f8b\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u7528\u4f8b\u63cf\u8ff0', blank=True)),
                ('level', models.IntegerField(verbose_name='\u7528\u4f8b\u7b49\u7ea7', choices=[(1, '\u4f4e'), (2, '\u4e2d'), (3, '\u9ad8')])),
                ('command', models.TextField(max_length=255, null=True, verbose_name='\u547d\u4ee4')),
                ('script', models.TextField(max_length=255, null=True, verbose_name='\u811a\u672c')),
                ('param', models.TextField(max_length=255, null=True, verbose_name='\u53c2\u6570')),
                ('createdAt', models.DateTimeField(verbose_name='\u521b\u5efa\u7684\u65f6\u95f4')),
                ('modifyAt', models.DateTimeField(auto_now_add=True, verbose_name='\u4fee\u6539\u7684\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='Case_Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.IntegerField(default=3, verbose_name='\u7ed3\u679c', choices=[(1, 'pass'), (2, 'fail'), (3, 'running'), (4, 'finish')])),
                ('case', models.ForeignKey(to='appmanager.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='\u4e3b\u673a\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u4e3b\u673a\u63cf\u8ff0', blank=True)),
                ('address', models.IPAddressField(verbose_name='IP')),
                ('status', models.IntegerField(default=2, verbose_name='\u4e3b\u673a\u72b6\u6001', choices=[(1, '\u5728\u7ebf'), (2, '\u79bb\u7ebf')])),
                ('createdAt', models.DateTimeField(verbose_name='\u521b\u5efa\u7684\u65f6\u95f4')),
                ('modifyAt', models.DateTimeField(auto_now_add=True, verbose_name='\u4fee\u6539\u7684\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='Suite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='\u5957\u4ef6\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u5957\u4ef6\u63cf\u8ff0', blank=True)),
                ('createdAt', models.DateTimeField(verbose_name='\u521b\u5efa\u7684\u65f6\u95f4')),
                ('modifyAt', models.DateTimeField(auto_now_add=True, verbose_name='\u4fee\u6539\u7684\u65f6\u95f4')),
                ('cases', models.ManyToManyField(to='appmanager.Case', null=True, blank=True)),
                ('suites', models.ManyToManyField(to='appmanager.Suite', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u4efb\u52a1\u63cf\u8ff0', blank=True)),
                ('createdAt', models.DateTimeField(verbose_name='\u521b\u5efa\u7684\u65f6\u95f4')),
                ('modifyAt', models.DateTimeField(auto_now_add=True, verbose_name='\u4fee\u6539\u7684\u65f6\u95f4')),
                ('suite', models.ForeignKey(to='appmanager.Suite')),
            ],
        ),
        migrations.CreateModel(
            name='Task_Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u7684\u65f6\u95f4')),
                ('case', models.ForeignKey(to='appmanager.Case')),
                ('task', models.ForeignKey(to='appmanager.Suite')),
            ],
        ),
        migrations.CreateModel(
            name='Task_Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.IntegerField(default=3, verbose_name='\u7ed3\u679c', choices=[(1, 'pass'), (2, 'fail'), (3, 'running'), (4, 'finish')])),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u7684\u65f6\u95f4')),
                ('machine', models.ForeignKey(to='appmanager.Machine')),
                ('task', models.ForeignKey(to='appmanager.Suite')),
            ],
        ),
        migrations.AddField(
            model_name='case_report',
            name='task_report',
            field=models.ForeignKey(to='appmanager.Task_Report'),
        ),
    ]
