from django import forms
from .models import NewPost, NewExercise
class NewPostForm(forms.ModelForm):
    class Meta:
        model = NewPost
        fields = ('title', 'body', 'public', 'image')

class NewExerciseForm(forms.ModelForm):
    class Meta:
        model = NewExercise
        fields = ('name', 'reps', 'sets', 'notes')