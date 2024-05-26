from django import forms
from .models import Document

class documentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'file',)
