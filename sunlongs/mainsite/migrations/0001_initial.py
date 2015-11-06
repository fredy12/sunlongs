# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('intro', models.CharField(default=b'', max_length=100)),
                ('content', models.TextField(default=b'')),
                ('type', models.CharField(max_length=50, null=True, blank=True)),
                ('tag', models.CharField(max_length=50, null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('lang', models.CharField(max_length=20, null=True, blank=True)),
                ('short_name', models.CharField(max_length=50, null=True, blank=True)),
                ('full_name', models.CharField(max_length=200, null=True, blank=True)),
                ('abstract', models.CharField(max_length=500, null=True, blank=True)),
                ('introduction', models.TextField(null=True, blank=True)),
                ('culture', models.TextField(null=True, blank=True)),
                ('application', models.TextField(null=True, blank=True)),
                ('business', models.TextField(null=True, blank=True)),
                ('certificate_info', models.TextField(null=True, blank=True)),
                ('contact_num', models.CharField(max_length=20, null=True, blank=True)),
                ('contact_name', models.CharField(max_length=50, null=True, blank=True)),
                ('order_num', models.CharField(max_length=20, null=True, blank=True)),
                ('fax_num', models.CharField(max_length=20, null=True, blank=True)),
                ('address', models.CharField(max_length=500, null=True, blank=True)),
                ('postcode', models.CharField(max_length=10, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('additional', models.CharField(max_length=100, null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('file_info', models.FileField(upload_to=b'file')),
                ('display_name', models.CharField(max_length=100, null=True, blank=True)),
                ('description', models.CharField(max_length=100, null=True, blank=True)),
                ('media_type', models.CharField(default=b'image', max_length=50, null=True, blank=True)),
                ('type', models.CharField(max_length=50, null=True, blank=True)),
                ('tag', models.CharField(max_length=50, null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('lang', models.CharField(max_length=20, null=True, blank=True)),
                ('title', models.CharField(max_length=150)),
                ('intro', models.CharField(default=b'', max_length=100)),
                ('content', models.TextField(default=b'')),
                ('type', models.CharField(max_length=50, null=True, blank=True)),
                ('tag', models.CharField(max_length=50, null=True, blank=True)),
                ('status', models.BooleanField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('lang', models.CharField(max_length=20, null=True, blank=True)),
                ('standard', models.CharField(max_length=50, null=True, blank=True)),
                ('market', models.CharField(max_length=20, null=True, blank=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('pic', models.ImageField(null=True, upload_to=b'product', blank=True)),
                ('model', models.CharField(max_length=50, null=True, blank=True)),
                ('power', models.CharField(max_length=20, null=True, blank=True)),
                ('flow', models.CharField(max_length=20, null=True, blank=True)),
                ('head', models.CharField(max_length=20, null=True, blank=True)),
                ('voltage', models.CharField(max_length=20, null=True, blank=True)),
                ('outlet', models.CharField(max_length=20, null=True, blank=True)),
                ('speed', models.CharField(max_length=20, null=True, blank=True)),
                ('eff', models.CharField(max_length=20, null=True, blank=True)),
                ('abstract', models.CharField(max_length=500, null=True, blank=True)),
                ('feature', models.CharField(max_length=500, null=True, blank=True)),
                ('introduction', models.TextField(null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('lang', models.CharField(max_length=20, null=True, blank=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('introduction', models.CharField(max_length=500, null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VisitInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('number', models.IntegerField(null=True, blank=True)),
                ('type', models.CharField(max_length=20, null=True, blank=True)),
                ('page', models.CharField(max_length=20, null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='productinfo',
            name='type',
            field=models.ForeignKey(to='mainsite.ProductType'),
        ),
    ]
