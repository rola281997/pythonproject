from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from .models import post,Category,forbWords,notify,Comment,Likes
from .forms import UserForm,PostForm,CategoryForm,wordForm,contactAdmin,SignUpForm,CommentForm
from django.db import transaction
from PIL import Image
import json
import datetime
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.core.exceptions import  ValidationError
from django.contrib.auth import login, authenticate, logout
from django.core.files.storage import FileSystemStorage
from django.template import RequestContext

# Create your views here.

@login_required
def index(request):
    if(request.user.is_staff):
        all_users = User.objects.all()
        all_posts = post.objects.all()
        all_cats = Category.objects.all()
        all_words=forbWords.objects.all()
        context = {'all_users':all_users,'all_posts':all_posts,'all_cats':all_cats,'all_words':all_words}
        return render(request,'base_site.html',context)
    else:
        return redirect('login')


def viewUser(request,id):
    user=User.objects.get(id=id)
    context={'user':user}
    return render(request,'viewUser.html',context)


def blockUser(request,id):
    user=User.objects.get(id=id)
    user.is_active= '0'
    user.save()
    transaction.commit()
    return HttpResponseRedirect('/users')


def unblockUser(request,id):
    user=User.objects.get(id=id)
    user.is_active=  1 
    user.save()
    transaction.commit()
    return HttpResponseRedirect('/users')


def all_users(request):
    all_users =User.objects.all()
    context = {'all_users':all_users}
    return render(request,'all_users.html',context)

def addUser(request):
    user=UserForm()
    if(request.method=='POST'):
        user=UserForm(request.POST)
        if(user.is_valid()):
            user.save()
            return HttpResponseRedirect('/users')
    else:
        context={'user':user}
        return render (request,'userForm.html',context)

def updateUser(request,id):
    user=User.objects.get(id=id)
    if(request.method=='POST'):
        user_form=UserForm(request.POST,instance=user)
        if(user_form.is_valid()):
            user_form.save()
            return HttpResponseRedirect('/users')
    else:
        user_form=UserForm(instance=user)
        context={'user':user_form}
        return render(request,'userForm.html',context)

def delete(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect('/users')

def setAdmin(request,id):
    user=User.objects.get(id=id)
    if(user.is_active == 0):
        user.is_active = 1
        user.is_staff =  1
        user.save()
        transaction.commit()
        return HttpResponseRedirect('/users')
    else:
        user.is_staff = 1
        user.save()
        transaction.commit()
        return HttpResponseRedirect('/users')

#for rolaa u can use it to check wheather this user is blocked or not 


# def blocked(request):
#     username=User.objects.get(username=request.POST['username'])
#     if(username  is not None):
#         messages.warning(request,'hereeeeeeeee')
#         if(username.password == request.POST['password']):
#             if(username.is_active ==1 ):
#                 return HttpResponseRedirect('/Post/single')
#             else:
#                 contact=contactAdmin()
#                 if(request.method=='Post'):
#                     contact=contactAdmin(request.POST)
#                     if(contact.is_valid()):
#                         contact.save()
#                         return HttpResponseRedirect('/Post/single')
#                 else:
#                     context={'notify':notify}
#                     return render (request,'contactAdmin.html',context)
#         else:
#             messages.warning(request,"wrong password")
#     else:
#         messages.warning(request,"user name not valid")

                # return HttpResponseRedirect('/cont')



#POST

def viewPost(request,id):
    wantedPost=post.objects.get(id=id)
    context={'post':wantedPost}
    return render(request,'viewPost.html',context)

def allPosts(request):
    all_posts = post.objects.all()
    context = {'all_posts':all_posts}
    return render(request,'all_posts.html',context)

def addpost(request):
    post=PostForm()
    if(request.method=='POST'):
        post=PostForm(request.POST,request.FILES)
        if(post.is_valid()):
            post.save()
            return HttpResponseRedirect('/posts')
    else:
        context={'post':post}
        return render (request,'postform.html',context)

def updatePost(request,id):
    wantedPost=post.objects.get(id=id)
    if(request.method=='POST'):
        post_form=PostForm(request.POST,instance=wantedPost)
        if(post_form.is_valid()):
            post_form.save()
            return HttpResponseRedirect('/posts')
    else:
        post_form=PostForm(instance=wantedPost)
        context={'post':post_form}
        return render(request,'postform.html',context)

def deletePost(request,id):
    WantedPost=post.objects.get(id=id)
    WantedPost.delete()
    return HttpResponseRedirect('/posts')


#Category

def viewCat(request,id):
    cat=Category.objects.get(id=id)
    context={'cat':cat}
    return render(request,'viewCat.html',context)

def all_cats(request):
    all_cats = Category.objects.all()
    context = {'all_cats':all_cats}
    return render(request,'all_cats.html',context)

def addCat(request):
    cat=CategoryForm()
    if(request.method=='POST'):
        cat=CategoryForm(request.POST)
        if(cat.is_valid()):
            cat.save()
            return HttpResponseRedirect('/cats')
    else:
        context={'cat':cat}
        return render (request,'catform.html',context)

def updateCat(request,id):
    cat=Category.objects.get(id=id)
    if(request.method=='POST'):
        cat_form=CategoryForm(request.POST,instance=cat)
        if(cat_form.is_valid()):
            cat_form.save()
            return HttpResponseRedirect('/cats')
    else:
        cat_form=CategoryForm(instance=cat)
        context={'cat':cat_form}
        return render(request,'catform.html',context)

def deleteCat(request,id):
    cat=Category.objects.get(id=id)
    cat.delete()
    return HttpResponseRedirect('/cats')
#add admin

def addAdmin(request): 
    admin=UserForm()
    if(request.method=='POST'):
        admin=UserForm(request.POST)
        if(admin.is_valid()):
            admin.save()
            return HttpResponseRedirect('/users')
    else:
        context={'admin':admin}
        return render (request,'adminform.html',context)       
#words
def all_words(request):
    words=forbWords.objects.all()
    context={'words':words}
    return render(request,'all_words.html',context)

def addWord(request):
    word=wordForm()
    if(request.method=='POST'):
        word=wordForm(request.POST)
        if(word.is_valid()):
            word.save()
            return HttpResponseRedirect('/words')
    else:
        context={'word':word}
        return render (request,'wordForm.html',context)


def deleteWord(request,id):
    word=forbWords.objects.get(id=id)
    word.delete()
    return HttpResponseRedirect('/words')


#notes de for rolaa : u can use it ya rolaa to view for blocked user to contact admin
def addNotification(request):
    notify=contactAdmin()
    if(request.method=='POST'):
        notify=contactAdmin(request.POST)
        if(notify.is_valid()):
            notify.save()
            return redirect('login')
    else:
        context={'notify':notify}
        return render(request,'contactAdmin.html',context)


#notes lya for admin to show notes 
def notes(request):
    notes=notify.objects.all()
    context={'notes':notes}
    return render(request,'all_notes.html',context)


#registration and login 

def home(request):
    all_post = post.objects.all().order_by("post_date").reverse()
    all_cat = Category.objects.all()
    if len(all_post)<=5:
        context = {'all_cat' : all_cat,'all_post' : all_post}
    else:
        fivePosts=all_post[:5]
        context = {'all_cat' : all_cat,'all_post' : fivePosts}
    return render (request , 'Post/single.html' , context)


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/single')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})



#
# def login_user(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#
#         if form.is_valid():
#             # flag = request.user.is_active
#             # if flag:
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#         # else:
#              # messages.warning(request, 'sryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
#
#     else:
#         form = LoginForm()
#     return render(request, 'registration/login.html', {
#         'form': form,
#     })

# def logout_user(request):
#     logout(request)
#     return render(request, 'registration/logout.html', {
#
#     })



#m7moud and mamdou7

# def all_categories(request):
#     all_cat = Category.objects.all()
#     context = {'all_cat' : all_cat}
#     return render (request , 'Post/single.html' , context)




# def post_by_category(request,Id):
#     cat = Category.objects.get(id=Id)
#     posts = post.objects.filter(Category_id=cat)
#     context = {'all_post_inCat' :posts,
#     'CatName':cat }
#     return render (request , 'Post/travel.html' , context)
 
# def show_comments(request,Id):
#     Post=get_object_or_404(post,pk=Id)
#     comment = Comment.objects.filter(owner=Post.id)
    
#     if request.method =='POST':
#         comment_form=CommentForm(request.POST or None)
#         if comment_form.is_valid():
#             content=request.POST.get('body')
#             comment=Comment.objects.create(owner=Post,author=request.user ,body=content )
#             comment.save()
#             comment = Comment.objects.filter(owner=Post.id)
            
#             comment_form = CommentForm()

#     else : 
#         comment_form=CommentForm()  
#     count = comment.count()
#     context = {'Post' : Post,'all_comments' : comment ,'count':count, 'comment_form': comment_form}
#     return render (request , 'Post/onePost.html' , context)

# def all_posts(request):
    
#     all_post = post.objects.all().order_by("post_date").reverse()
#     all_cat = Category.objects.all()
#     if len(all_post)<=5:
#         context = {'all_cat' : all_cat,'all_post' : all_post}
#     else:
#         fivePosts=all_post[:5]
#         context = {'all_cat' : all_cat,'all_post' : fivePosts}
#     return render (request , 'Post/single.html' , context)



#m7moud and m7moud tany

def all_categories(request):
    all_cat = Category.objects.all()
    context = {'all_cat' : all_cat}
    return render (request , 'Post/single.html' , context)




def post_by_category(request,Id):
    cat = Category.objects.get(id=Id)
    posts = post.objects.filter(Category_id=cat)
    context = {'all_post_inCat' :posts,
    'CatName':cat }
    return render (request , 'Post/travel.html' , context)
 
def show_comments(request,Id):
    Post=get_object_or_404(post,pk=Id)
    is_liked=None
    like = Likes.objects.filter(post_id=Id)
    post_likes = like.filter(like = True).count()
    post_dislikes = like.filter(like = False).count()
    if request.user.is_authenticated:
        like = Likes.objects.filter(post_id=Post, userId=request.user.id)

        if like.exists():
            if like.get().like == True:
                is_liked=True
            else:
                is_liked=False

   
   
   
    comment = Comment.objects.filter(owner=Post.id,reply=None)
    if request.method =='POST':
        comment_form=CommentForm(request.POST or None)
        if comment_form.is_valid():
            content=request.POST.get('body')
            reply_id=request.POST.get('comment_id')
            comment_qs=None
            if reply_id:
                comment_qs=Comment.objects.get(id=reply_id)
            comment=Comment.objects.create(owner=Post,author=request.user ,body=content, reply=comment_qs )
            comment.save()
            comment = Comment.objects.filter(owner=Post.id) 
            comment_form = CommentForm()

    else : 
        comment_form=CommentForm()  
    
    context = {'Post' : Post,'comments' : comment ,'comment_form': comment_form ,'post_likes': post_likes,'post_dislikes': post_dislikes,'is_liked': is_liked,}
    return render (request , 'Post/onePost.html' , context)
 
 
    
def all_posts(request):
    
    all_post = post.objects.all().order_by("post_date").reverse()
    all_cat = Category.objects.all()

###################################################

    # subs = Subscribe.objects.filter(subscriber_id = request.user).values_list('category_id', flat=True)
  
    # checks = Check(all_cat, subs)

####################################################


    if len(all_post)<=5:
        context = {'all_cat' : all_cat,'all_post' : all_post}
    else:
        fivePosts=all_post[:5]
        context = {'all_cat' : all_cat,'all_post' : fivePosts}
    return render (request , 'Post/single.html' , context)


@login_required
def like(request,post_id):
    print(request.user.id)
    print(post_id)
    if not Likes.objects.filter(post_id=post_id, userId=request.user.id).exists():
        Post = post.objects.get(id=post_id)
        print(Post)
        
        if request.POST.get('like') == '1':
            Likes.objects.create(post_id=Post, userId=request.user, like = True)
        else:
            Likes.objects.create(post_id=Post, userId=request.user, like = False)

        dislike = Likes.objects.filter(post_id=Post, like = False)
        if dislike.count() >= 10:
            # dislike.delete()
            Post.delete()

            return HttpResponseRedirect('/single/')
     
    return HttpResponseRedirect('/onePost/' + post_id)


def search(request):
    query = request.GET.get("q")
    print(query)
    # if query:
    Posts = post.objects.filter(title__icontains = query)
    print(Posts)
    context = {'Posts': Posts} 
    return render(request,'Post/search.html',context)




########################################################
# def subscribe(request, category_id):
#     try:
#         cat = Category.objects.get(id = category_id)
#         Subscribe.objects.create(subscriber_id = request.user, category_id = cat)
#     finally:
#         return HttpResponseRedirect('/')


# def unsubscribe(request,category_id):
#     try:
#         cat = Category.objects.get(id = category_id)
#         sub = Subscribe.objects.get(subscriber_id = request.user, category_id = cat)
#         sub.delete()
#     finally:
#         return HttpResponseRedirect('/')


# def Check(cats, subs):
#     Checks = []
#     for cat in cats:
#         # print(cat)
#         if cat.id in subs:
#             check = cat.id
#         else:
#             check = -1
#         Checks.append(check)
#     # print(Checks)
#     return Checks

#########################################################################