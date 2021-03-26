from django import forms
from .models import Blog
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'body']
        