# Generated by Django 3.1.5 on 2021-01-22 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animelist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='name',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='password',
            field=models.CharField(default=11111111, max_length=50),
            preserve_default=False,
        ),
    ]
