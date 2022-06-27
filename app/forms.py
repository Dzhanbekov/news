from .models import News
from django import forms


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'content', 'image']