# Generated by Django 4.1.7 on 2023-04-11 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=128),
        ),
    ]
