# Generated by Django 4.2.16 on 2024-11-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='bio',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
