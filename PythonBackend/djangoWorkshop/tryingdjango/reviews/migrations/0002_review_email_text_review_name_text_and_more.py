# Generated by Django 4.2.7 on 2023-12-08 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='email_text',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='review',
            name='name_text',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='review',
            name='number_text',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
