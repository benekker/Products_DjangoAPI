# Generated by Django 4.0.6 on 2022-07-14 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_random'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='random',
        ),
    ]