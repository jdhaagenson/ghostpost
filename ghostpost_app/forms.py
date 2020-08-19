from django import forms


class NewPostForm(forms.Form):
    is_boast = forms.BooleanField()
    content = forms.CharField(max_length=250)
