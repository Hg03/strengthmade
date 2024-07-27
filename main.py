import streamlit as st
import random

st.set_page_config(page_title='strenghtmade', page_icon='🛎️')

# Define the list of motivational thoughts
motivational_thoughts = {
    "Transform Your Body, One Swing at a Time": "Kettlebells are not just weights; they're tools for transformation. Every rep brings you closer to a stronger, fitter you.",
    "Embrace the Challenge, Reap the Reward": "The unique movements in kettlebell training push you out of your comfort zone, building resilience and strength.",
    "The Bell That Rings with Progress": "With each swing, press, and lift, kettlebells ring with the sound of your hard work and dedication.",
    "Strength Lies in Mastering the Basics": "Kettlebell training teaches you that mastery comes from perfecting the fundamentals, building a solid foundation.",
    "From Weakness to Strength, One Lift at a Time": "Kettlebells are the perfect tool for turning weaknesses into strengths, both physically and mentally.",
    "Unleash Your Inner Warrior": "Training with kettlebells is like training for battle—prepare your body and mind for whatever life throws at you.",
    "The Power of Consistency": "Just like any other skill, consistency in kettlebell training is key. Keep lifting, and watch your progress skyrocket.",
    "Sweat, Strength, Success": "The more you sweat in your kettlebell workouts, the stronger you become, leading you to success in all areas of life.",
    "A Journey of a Thousand Swings": "Every kettlebell session is a step on your fitness journey. Embrace the process and enjoy the ride.",
    "The Iron Bell, Your Silent Mentor": "The kettlebell may be silent, but it teaches invaluable lessons in discipline, perseverance, and growth."
}

# Pick a random motivational thought
random_title = random.choice(list(motivational_thoughts.keys()))
random_thought = motivational_thoughts[random_title]


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

# Display the random thought in an expander
with st.expander(random_title):
    st.write(random_thought)


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
