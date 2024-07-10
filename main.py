import random
import streamlit as st

# Define the exercise lists
upper_body_exercises = [
    "Kettlebell Snatch",
    "Kettlebell Zercher and Press",
    "Kettlebell Swing",
    "Kettlebell Halo",
    "Kettlebell Bent-Over Row",
]

lower_body_exercises = [
    "Kettlebell Goblet Squat",
    "Kettlebell Romanian Deadlift",
    "Kettlebell Lunge",
    "Kettlebell Kickstand Squat",
    "Kettlebell Deadlift",
]

full_body_exercises = [
    "Kettlebell Thrusters", 
    "Kettlebell Overhead Lunges",
    "Kettlebell Clean Squat"
]

# Function to generate a workout
def generate_workout(upper_count, lower_count, full_count):
    workout = []

    workout.extend(random.sample(upper_body_exercises, upper_count))
    workout.extend(random.sample(lower_body_exercises, lower_count))
    workout.extend(random.sample(full_body_exercises, full_count))

    return workout

# Streamlit app layout
st.title("Kettlebell Workout Generator")
st.image('kb.jpg', caption='You Are Savage💪')

st.sidebar.header("Workout Configuration")
upper_count = st.sidebar.slider("Number of Upper Body Exercises", 1, len(upper_body_exercises), 1)
lower_count = st.sidebar.slider("Number of Lower Body Exercises", 1, len(lower_body_exercises), 1)
full_count = st.sidebar.slider("Number of Full Body Exercises", 1, len(full_body_exercises), 1)

if st.sidebar.button("Generate Workout"):
    workout = generate_workout(upper_count, lower_count, full_count)
    st.subheader("Your Kettlebell Workout:")
    for i, exercise in enumerate(workout, start=1):
        st.write(f"Exercise {i}: {exercise}")

