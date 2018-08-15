from django import forms
from .models import PostComment
from ckeditor.widgets import CKEditorWidget

class NewPostCommentForm(forms.ModelForm):

    class Meta():
        model = PostComment
        fields = ('name', 'email', 'comment_body', 'post')
        labels = {
            'name': 'Name',
            'email': 'Email',
            'comment_body': 'Comment',
        }
        widgets = {
            'comment_body': forms.CharField(strip=True),
            'post': forms.HiddenInput(),
        }
