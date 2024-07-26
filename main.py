import streamlit as st
import random

# Define the exercise categories and their corresponding exercises
upper_push = {
    "Shoulder": ["Z Press", "Zercher Press", "Clean and Press", "Pike Push-Ups"],
    "Chest": ["Floor Press (60 Degree)", "Floor Press (90 Degree)", "Crush Grip Press", "Deficit Push-Ups"]
}

upper_pull = {
    "Upper Back and Whole Chain": ["Unilateral Rows", "Snatch (Front)", "Dead Snatch", "Pull-Ups"],
    "Traps and Whole Chain": ["Carryovers (Walk)", "Pullover", "High Pulls", "Snatch (Lateral/Rotational)"]
}

lower_push = {
    "Quads": ["Goblet Squat", "Lunges (One with Hold, One with Clean)", "Curtsy Lunges", "Zercher Squat"]
}

lower_pull = {
    "Hamstrings": ["RDL (Single Leg)", "RDL (Both Legs)", "Swings"]
}

# Streamlit app
st.title('Custom Kettlebell Workout Generator')

# Selection box for workout categories
selected_categories = st.multiselect(
    'Select two workout categories:', 
    ['Upper Body Push', 'Upper Body Pull', 'Lower Body Push', 'Lower Body Pull'],
    default=['Upper Body Push', 'Lower Body Push'],
    max_selections=2
)

# Function to pick exercises
def pick_exercise(category):
    return random.choice(category)

def pick_two_exercises(category):
    return random.sample(category, 2)

# Display selected workouts
if len(selected_categories) == 2:
    workout = []
    for category in selected_categories:
        if category == 'Upper Body Push':
            workout.append(pick_exercise(upper_push["Shoulder"]))
            workout.append(pick_exercise(upper_push["Chest"]))
        elif category == 'Upper Body Pull':
            workout.append(pick_exercise(upper_pull["Upper Back and Whole Chain"]))
            workout.append(pick_exercise(upper_pull["Traps and Whole Chain"]))
        elif category == 'Lower Body Push':
            workout.extend(pick_two_exercises(lower_push["Quads"]))
        elif category == 'Lower Body Pull':
            workout.extend(pick_two_exercises(lower_pull["Hamstrings"]))
    
    st.subheader('Your Workout:')
    for exercise in workout:
        st.write(f"- {exercise}")
else:
    st.write("Please select exactly two categories.")
