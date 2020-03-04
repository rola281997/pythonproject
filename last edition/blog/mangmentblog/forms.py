from django import forms
from .models import Category,post,forbWords,notify,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms import PasswordInput
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']


class PostForm(forms.ModelForm):
    class Meta:
        model=post
        fields=['title','content','post_date','Owner','Category_id','image']
    
class wordForm(forms.ModelForm):
    class Meta:
        model=forbWords
        fields=['word']


class contactAdmin(forms.ModelForm):
    class Meta:
        model=notify
        fields=['notifSender','notifContent']


# rolaa forms
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']).exists():
            raise forms.ValidationError("Email exists")
        return cd['email']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError("username exists")
        return cd['username']

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': (
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive':  ("please connect with admin your account is blocked."),
    }

#m7moud and mamdou7
class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

