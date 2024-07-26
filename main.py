import streamlit as st
import random

st.set_page_config(page_title='strenghtmade', page_icon='🛎️')

# Define the exercise categories and their corresponding exercises with details
upper_push = {
    "Shoulder": {
        "Z Press": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/z_press"},
        "Zercher Press": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/zercher_press"},
        "Clean and Press": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/clean_and_press"},
        "Pike Push-Ups": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/pike_push_ups"}
    },
    "Chest": {
        "Floor Press (60 Degree)": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/floor_press_60"},
        "Floor Press (90 Degree)": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/floor_press_90"},
        "Crush Grip Press": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/crush_grip_press"},
        "Deficit Push-Ups": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/deficit_push_ups"}
    }
}

upper_pull = {
    "Upper Back and Whole Chain": {
        "Unilateral Rows": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/unilateral_rows"},
        "Snatch (Front)": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/snatch_front"},
        "Dead Snatch": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/dead_snatch"},
        "Pull-Ups": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/pull_ups"}
    },
    "Traps and Whole Chain": {
        "Carryovers (Walk)": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/carryovers_walk"},
        "Pullover": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/pullover"},
        "High Pulls": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/high_pulls"},
        "Snatch (Lateral/Rotational)": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/snatch_lateral"}
    }
}

lower_push = {
    "Quads": {
        "Goblet Squat": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/goblet_squat"},
        "Lunges (One with Hold, One with Clean)": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/lunges"},
        "Curtsy Lunges": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/curtsy_lunges"},
        "Zercher Squat": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/zercher_squat"}
    }
}

lower_pull = {
    "Hamstrings": {
        "RDL (Single Leg)": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/rdl_single_leg"},
        "RDL (Both Legs)": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/rdl_both_legs"},
        "Swings": {"sets": 3, "reps": "8-12", "demo_link": "https://example.com/swings"}
    }
}

# Streamlit app
st.title('Kettlebell Workout Recommender')

# Selection box for workout categories
selected_categories = st.multiselect(
    'Select two workout categories:', 
    ['Upper Body Push', 'Upper Body Pull', 'Lower Body Push', 'Lower Body Pull'],
    default=['Upper Body Push', 'Lower Body Push'],
    max_selections=2
)

# Function to pick exercises
def pick_exercise(category):
    return random.choice(list(category.items()))

def pick_two_exercises(category):
    return random.sample(list(category.items()), 2)

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
    for exercise, details in workout:
        with st.expander(exercise):
            st.write(f"Sets: {details['sets']}")
            st.write(f"Reps: {details['reps']}")
            st.link_button(label="Demo Link", url=details['demo_link'])
else:
    st.write("Please select exactly two categories.")
