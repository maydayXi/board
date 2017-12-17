from django import forms
from captcha.fields import CaptchaField

class PostForm(forms.Form):
    board_title = forms.CharField(max_length=100, initial='')
    board_name = forms.CharField(max_length=20, initial='')
    board_gender = forms.BooleanField()
    board_mail = forms.EmailField(max_length=100, initial='', required=False)
    board_web = forms.URLField(max_length=100, initial='', required=False)
    board_content = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()
