# Generated by Django 5.0.7 on 2024-08-18 13:43

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('BLOG', 'Blog'), ('NEWS', 'News')], max_length=4, verbose_name='Content')),
                ('blog_name', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=1000)),
                ('descriptions', django_ckeditor_5.fields.CKEditor5Field(max_length=30000)),
                ('tags', models.CharField(max_length=256)),
                ('count_views', models.PositiveIntegerField(default=0)),
                ('post_by', models.CharField(max_length=64)),
                ('hero_image', models.FileField(upload_to='images/hero/%y/%m/%d/')),
                ('blog_image', models.FileField(upload_to='images/blog/%y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'BlogNews',
            },
        ),
    ]
