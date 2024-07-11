import random
import streamlit as st

# Define the exercise lists

"""
shoulder -
    - kettlebell zercher and press
    - kettlebell clean and press
    - kettlebell z press
    - pike push ups

chest -
    - kettlebell Floor press (lower)
    - kettlebell crush grip press (both arms)
    - push ups
    - kettlebell 90 degree floor press (upper) 

back -
    - pull ups
    - kettlebell rows
    - kettlebell snatch
    - kettlebell snatchy lunges

legs - 
    - double kettlebell (one clean and one hanged) lunges
    - kang squat
    - kettlebell curtsy squat
    - Romanian deadlift

Full body - 
    - kettlebell Overhead squat
    - thrusters
    - kettlebell swing
    - burpees
"""
upper_body_exercises = {
    "Kettlebell Snatch": "https://youtu.be/6l2Iu26oWW8?si=N_Tgsker1xrITWrg",
    "Kettlebell Zercher and Press": "https://youtube.com/shorts/rEmwZw2blqs?si=0_0Z1AcocynfUIDp",
    "Kettlebell Swing": "https://youtu.be/ae6nV6pFRG4?si=fpSZaDpJ8KpGaemZ",
    "Kettlebell Halo": "https://youtu.be/Zy6bgAxPeks?si=1E8lv137u0f-CMrr",
    "Kettlebell Bent-Over Row": "https://youtu.be/9Q9gwoXHn1o?si=VUXCZcoBgc9VuxRP",
}

lower_body_exercises = {
    "Kettlebell Goblet Squat": "https://youtu.be/7EGVKUH0K10?si=aN1EUEJj2nSG54oQ",
    "Kettlebell Romanian Deadlift": "https://youtu.be/keiZFdUgvKQ?si=ZTbZO5AT7ZPdmnby",
    "Kettlebell Lunge": "https://youtube.com/shorts/CEeb-FqLmwk?si=ZyabS3ky6-q8-01U",
    "Kettlebell Kickstand Squat": "https://youtube.com/shorts/QvXbpnGayzw?si=m3XQyrtU08R-5-jv",
    "Kettlebell Deadlift": "https://youtu.be/G8wX8wwDJsM?si=fx8JAFEnTBmUl_WM",
}

full_body_exercises = {
    "Kettlebell Thrusters": "https://youtube.com/shorts/Id0Qefh4AHc?si=xj6yu7Ud1xUsVlYj", 
    "Kettlebell Overhead Lunges": "https://youtu.be/EDK2KTVPHU0?si=tz_IY0r4LZpwkVji",
    "Kettlebell Clean Squat": "https://youtu.be/yXTH9_7imAQ?si=IYTtM2StXMav2ikm"
}

# Function to generate a workout
def generate_workout(upper_count, lower_count, full_count):
    workout = []
    demos = []

    upper_exercises = random.sample(list(upper_body_exercises.keys()), upper_count)
    lower_exercises = random.sample(list(lower_body_exercises.keys()), lower_count)
    full_exercises = random.sample(list(full_body_exercises.keys()), full_count)

    for exercise in upper_exercises:
        workout.append(exercise)
        demos.append(upper_body_exercises[exercise])
    
    for exercise in lower_exercises:
        workout.append(exercise)
        demos.append(lower_body_exercises[exercise])

    for exercise in full_exercises:
        workout.append(exercise)
        demos.append(full_body_exercises[exercise])

    return workout, demos

# Streamlit app layout
st.title("Kettlebell Workout Generator")
st.image('kb.jpg', caption='You Are Savage💪')

st.sidebar.header("Workout Configuration")
upper_count = st.sidebar.slider("Number of Upper Body Exercises", 1, len(upper_body_exercises), 1)
lower_count = st.sidebar.slider("Number of Lower Body Exercises", 1, len(lower_body_exercises), 1)
full_count = st.sidebar.slider("Number of Full Body Exercises", 1, len(full_body_exercises), 1)

if st.button("Generate Your Savage Workout"):
    workout, demos = generate_workout(upper_count, lower_count, full_count)
    st.info("Your Kettlebell Workout:")
    for i, (exercise, demo) in enumerate(zip(workout, demos), start=1):
        with st.expander(f"Exercise {i}: {exercise}"):
            st.write("3x sets with 8-10x reps")
            st.link_button("How you can do it", demo)
