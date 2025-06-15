from django import forms

from blog.models import Comment
from mysite.settings import EMAIL_HOST_USER


# https://docs.djangoproject.com/en/5.2/topics/forms/
# https://docs.djangoproject.com/en/5.2/ref/forms/fields/
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField(initial=EMAIL_HOST_USER)
    to = forms.EmailField()
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea,
    )


# https://docs.djangoproject.com/en/5.2/topics/forms/modelforms/
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
