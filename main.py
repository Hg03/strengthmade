import streamlit as st
import random

# Set page title and icon
st.set_page_config(page_title='StrengthMade', page_icon='🛎️')

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

# Streamlit app title and motivational message
st.title('Kettlebell Workout Recommender')
st.subheader(random_title)
st.write(random_thought)

# List of exercises
exercises = {
    "Push Ups": {"Sets": "4", "Reps": "8-10"},
    "Pull Ups": {"Sets": "4", "Reps": "8-10"},
    "Handstand Push Ups": {"Sets": "4", "Reps": "8"},
    "Kettlebell Chest Press": {"Sets": "4", "Reps": "8-10"},
    "Kettlebell Shoulder Press": {"Sets": "4", "Reps": "6-8"},
    "Kettlebell Rows": {"Sets": "4", "Reps": "8-10"},
    "Kettlebell Swings": {"Sets": "4", "Reps": "8-10"},
    "Kettlebell Snatch": {"Sets": "4", "Reps": "4-5"},
    "Kettlebell Goblet Squats": {"Sets": "4", "Reps": "8-10"},
    "Kettlebell Romanian Deadlift": {"Sets": "4", "Reps": "6-8"},
    "Kettlebell Clean Squats": {"Sets": "4", "Reps": "8-10"},
    "Kettlebell Clean Lunges": {"Sets": "4", "Reps": "8-10"},
    "Kettlebell Curls": {"Sets": "4", "Reps": "8-10"},
    "Kettlebell Tricep Extension": {"Sets": "4", "Reps": "8-10"}
}

# Function to generate a 5-day workout split
def generate_workout_split(exercises):
    all_exercises = list(exercises.keys())
    
    # Randomly select 10 exercises for the week
    selected_exercises = random.sample(all_exercises, 10)
    
    # Ensure each selected exercise appears twice
    exercises_pool = selected_exercises * 2
    
    # Shuffle the exercises pool
    random.shuffle(exercises_pool)
    
    # Split exercises into 5 days (4 exercises per day)
    split = [exercises_pool[i:i+4] for i in range(0, len(exercises_pool), 4)]
    
    # Output the workout program for 5 days
    workout_program = {}
    for i, day in enumerate(split[:5]):  # Take only the first 5 days
        day_key = f"Day {i + 1}"
        workout_program[day_key] = []
        for exercise in day:
            sets = exercises[exercise]["Sets"]
            reps = exercises[exercise]["Reps"]
            workout_program[day_key].append(f"{exercise}: {sets} sets x {reps} reps")
    return workout_program

# Generate the workout split
workout_split = generate_workout_split(exercises)

# Display the workout program for the week
for day, exercises in workout_split.items():
    st.header(day)
    for exercise in exercises:
        st.write(f"- {exercise}")
