# Generated by Django 3.0.6 on 2020-05-14 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_login_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='date',
            field=models.DateTimeField(verbose_name='Date Published'),
        ),
    ]
