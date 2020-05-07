from django import forms


class PostForm(forms.Form):
    post_name = forms.CharField(max_length=256)
    post_text = forms.CharField(widget=forms.Textarea)
    post_image = forms.ImageField()
