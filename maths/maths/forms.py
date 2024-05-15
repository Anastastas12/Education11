from django import forms
from .models import MathTask

class MathTaskForm(forms.ModelForm):
    class Meta:
        model = MathTask
        fields = ['title', 'description', 'correct_answer']
