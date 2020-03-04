# Generated by Django 3.0.3 on 2020-02-27 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mangmentblog', '0002_forbwords'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('reply_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent_id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='postCat',
        ),
        migrations.AddField(
            model_name='post',
            name='Category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mangmentblog.Category'),
        ),
        migrations.AddField(
            model_name='post',
            name='dislike_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='Owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to='open_img/'),
        ),
        migrations.DeleteModel(
            name='person',
        ),
        migrations.AddField(
            model_name='reply',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangmentblog.Comment'),
        ),
    ]
