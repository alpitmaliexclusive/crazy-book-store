import json
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_json_widget.widgets import JSONEditorWidget
from .models import Book, Entry, Review, Topic

class SignUpForm(UserCreationForm):
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
 class Meta:
  model = User
  fields = ['username', 'first_name', 'last_name', 'email']
  labels = {'email': 'Email'}

class EditUserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
        
class BookForm(forms.ModelForm):
     author = forms.JSONField(max_length=1024)

     class Meta:
       model = Book
       fields = "__all__"
       widgets = {
            'author': JSONEditorWidget
        }

          
class ReviewForm(forms.ModelForm):
  
  class Meta:
       model = Review
       fields = "__all__"


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = "__all__"        



