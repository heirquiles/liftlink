# Lift Link 

## Project Overview
Workout tracking and sharing app to help eliminate the need for notebooks and notes apps while you're in the gym.

****************************************************************

## Functionality
The User will be met with a form allowing them to track their exercises, including the weight used, number of sets, number of repetitions, and any notes they may have. Once workouts are saved, the option to share them with other users either publicly or by group will become available in-app or to their own social media via external share links. 

****************************************************************

## Data Models
NewExercise model with date of exercise, exercise name, sets, repetitions, and notes.

Workout model that groups exercises and tracks "Personal Records" for each exercise.

User model built into Django that allows saving user profiles

Group model with group name and members

Forum model with posts, comments, images and videos.

****************************************************************

## Schedule
### Week 1
Start Django app, and build user model and exercise model/forms

Build user profile page and exercise input pages. Use API for exercise suggestions as you input.(Possibly Exercise DB)

Build Forum model
### Week 2
Create workout model and logic for recording PRs for each exercise. 

Create Group model and logic for adding members to group as well as a feed or forum for group members to share exercise tips and personal bests.

Add support to for images and videos in Forum model
### Week 3
Styling with options for light and dark modes

****************************************************************

### Nice-to-Haves
Group specific notifications
Exercise instructional catalog
1RM Calculator
Initial PR input page
Nutrition input page and plans
Group challenges
