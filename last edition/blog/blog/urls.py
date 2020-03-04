"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include,re_path
from mangmentblog import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout_then_login
from mangmentblog import forms
from django.conf import settings
from django.contrib.auth import views as authView

urlpatterns = [
    path('adminIndex',views.index),
    path('user/<id>',views.viewUser),
    path('users',views.all_users),
    path('post/<id>',views.viewPost),
    path('posts',views.allPosts),
    path('cats',views.all_cats),
    path('cat/<id>',views.viewCat),
    path('addUser',views.addUser),
    path('addCat',views.addCat),
    path('addPost',views.addpost),
    path('updateUser/<id>',views.updateUser),
    path('updateCat/<id>',views.updateCat),
    path('updatePost/<id>',views.updatePost),
    path('deleteUser/<id>',views.delete),
    path('deleteCat/<id>',views.deleteCat),
    path('deletePost/<id>',views.deletePost),
    path('blockUser/<id>',views.blockUser),
    path('unblockUser/<id>',views.unblockUser),
    path('setadmin/<id>',views.setAdmin),
    path('words',views.all_words),
    path('addWord',views.addWord),
    path('contact',views.addNotification),
    path('deleteWord/<id>',views.deleteWord),
    path('notes',views.notes),
    #rolaa pathes
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('logout/',authView.LogoutView.as_view(),name='logout'),
    path('login/', LoginView.as_view(template_name='registration/login.html', authentication_form=forms.CustomAuthenticationForm), name='login'),
    #m7moud and mamdou7 pathes
    path('single/',views.all_posts),
    path('travel/<Id>',views.post_by_category),
    path('onePost/<Id>',views.show_comments),
    path('onePost/like/<post_id>',views.like),
    re_path(r'^[a-zA-Z/]*search/',views.search),
    # path('sub/<category_id>/', views.subscribe, name ='subscribe'),
    # path('unsub/<category_id>/', views.unsubscribe, name ='unsubscribe'),
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
