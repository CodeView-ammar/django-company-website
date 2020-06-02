# Generated by Django 2.2.11 on 2020-06-01 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_is_removed'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_removed',
            field=models.BooleanField(default=False, verbose_name='Is Removed'),
        ),
        migrations.AddField(
            model_name='tag',
            name='is_removed',
            field=models.BooleanField(default=False, verbose_name='Is Removed'),
        ),
    ]