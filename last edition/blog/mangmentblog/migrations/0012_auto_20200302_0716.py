# Generated by Django 3.0.3 on 2020-03-02 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangmentblog', '0011_auto_20200302_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to='open_img/'),
        ),
    ]
