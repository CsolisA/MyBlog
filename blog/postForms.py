from django import forms

from blog.models import Post


class postForm(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput)
    subtitle = forms.CharField(label="Sub Title", widget=forms.TextInput)
    body = forms.CharField(label="Body", widget=forms.TextInput)
    image = forms.CharField(label="Image URL", widget=forms.URLInput)

    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'body', 'image']

        # Help Messages
        help_texts = {k: "" for k in fields}
