from django import forms
from .models import Game, Review

class GameForm(forms.ModelForm):
    class Meta:
        model=Game
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'