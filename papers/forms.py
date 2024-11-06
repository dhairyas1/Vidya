from django import forms
from .models import Comment, ResearchPaper

class ResearchPaperForm(forms.ModelForm):
    class Meta:
        model = ResearchPaper
        fields = ['title', 'author', 'file','abstract']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']