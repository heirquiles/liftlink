from django import forms
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
    exercises = forms.ModelMultipleChoiceField(
    queryset = NewExercise.objects.all()
    )

 

# class NewWorkoutForm(forms.ModelForm):
#     class Meta:
#         model = NewWorkout
#         fields = ('title', 'exercises')
    
#     date = forms.DateInput()

#     exercises = forms.CharField