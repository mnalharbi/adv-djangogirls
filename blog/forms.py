from django import forms
from ckeditor.fields import RichTextFormField

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
          model = Post
          fields = ['title','text']
          widgets = {
             'text': RichTextFormField(),
          }
