from django import forms
from .models import Post

class blogForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
            "title",
            "description",
        ]