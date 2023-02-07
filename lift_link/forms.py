from django import forms
from django.forms import modelformset_factory
from .models import NewPost, NewExercise, NewWorkout
class NewPostForm(forms.ModelForm):
    class Meta:
        model = NewPost
        
        fields = ('title', 'body', 'public', 'image')

class NewExerciseForm(forms.ModelForm):
    class Meta:
        model = NewExercise
        fields = ('name', 'reps', 'sets', 'notes')

class NewWorkoutForm(forms.Form):
    title = forms.CharField(max_length=100)

ExerciseFormSet = modelformset_factory(
    NewExercise, fields=("name", "reps", "sets", "notes"), extra=1
)