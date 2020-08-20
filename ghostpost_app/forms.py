from django import forms


class NewPostForm(forms.Form):
    is_boast = forms.BooleanField()
    content = forms.CharField(widget=forms.Textarea)
