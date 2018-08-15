from django import forms
from .models import PostComment
from ckeditor.widgets import CKEditorWidget
from captcha.fields import CaptchaField

class NewPostCommentForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta():
        model = PostComment
        fields = ('name','email','comment_body','post')
        labels = {
            'name': 'Name',
            'email': 'Email',
            'comment_body': 'Comment',
            'captcha':'Anti Spam',
        }
        widgets = {
            'comment_body': forms.CharField(strip=True),
            'post': forms.HiddenInput(),
        }
        #CKEditorWidget(config_name='awesome_ckeditor')
