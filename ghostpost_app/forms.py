from django import forms
from ghostpost_app.models import Post

CHOICES = (
    (True, 'Boast'),
    (False, 'Roast')
)

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('is_boast', 'content')
        widgets = {
            'is_boast': forms.Select(choices=CHOICES),
            'content': forms.TextInput()
        }


