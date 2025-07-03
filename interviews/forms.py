from django import forms
from .models import Question, JobRole


class QuestionForm(forms.ModelForm):
    answer_text = forms.CharField(widget=forms.Textarea, label="Answer")

    class Meta:
        model = Question
        fields = ["job_role", "text"]
