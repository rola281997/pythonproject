# from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from datetime import datetime
from django.conf import settings
from CommandNotFound.db import db
from django.db import models
from django.contrib.auth.models import User

     

class Category(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name


class post(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now, null=False)
    image = models.ImageField(upload_to='open_img/',null=True)
    Owner=models.ForeignKey(User,on_delete=models.DO_NOTHING)    
    Category_id = models.ForeignKey(Category,null = True ,on_delete=models.SET_NULL)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class forbWords(models.Model):
    word=models.CharField(max_length=50)

class notify(models.Model):
    notifSender=models.CharField('Ur name',max_length=50)
    notifContent=models.CharField('Objection details',max_length=200)
    note_date=models.DateTimeField(default=timezone.now,null=False)

#m7moud and mamdou7

# class Comment(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE ,null=True)
#     id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
#     owner = models.ForeignKey(post, on_delete=models.CASCADE)
#     body = models.TextField()
#     comment_date = models.DateTimeField(default=timezone.now,null=False)
#     active = models.BooleanField(default=False) 
    




# class Reply(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
#     id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
#     owner = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     body = models.TextField()
#     reply_date = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=False) 



#mamdou7 and m7moud tany

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    owner = models.ForeignKey(post, on_delete=models.CASCADE)
    body = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False) 
    reply = models.ForeignKey('self',null=True,related_name='replies',on_delete= models.CASCADE)

class Likes(models.Model):
    like=models.BooleanField()
    userId=models.ForeignKey(User,on_delete= models.CASCADE)
    post_id=models.ForeignKey(post,on_delete= models.CASCADE)
    



#######################################################

# class Subscribe(models.Model):
#     category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
#     subscriber_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     class Meta:
#         unique_together = ["category_id", "subscriber_id"]
#     def __str__(self):
#         return '{} subscribe to {}'.format(self.subscriber_id, self.category_id)

###########################################################
