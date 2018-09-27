from django import forms
from .models import Feedback

class FeedbackModelForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ['create_date']