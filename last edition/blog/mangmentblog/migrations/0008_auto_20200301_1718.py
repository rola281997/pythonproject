# Generated by Django 3.0.3 on 2020-03-01 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangmentblog', '0007_auto_20200301_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='open_img/'),
        ),
    ]