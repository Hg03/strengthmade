import streamlit as st
import random

# Set page title and icon
st.set_page_config(page_title='StrengthMade', page_icon='🛎️', layout="wide")


# Define the list of motivational thoughts
motivational_thoughts = {
    "Transform Your Body, One Swing at a Time": "Kettlebells are not just weights; they're tools for transformation. Every rep brings you closer to a stronger, fitter you.",
    "Embrace the Challenge, Reap the Reward": "The unique movements in kettlebell training push you out of your comfort zone, building resilience and strength.",
    # Add more motivational thoughts...
}

# Pick a random motivational thought
random_title = random.choice(list(motivational_thoughts.keys()))
random_thought = motivational_thoughts[random_title]

# Streamlit app title and motivational message
st.title('Kettlebell Workouts')
st.image('coffeexbell.png')
st.subheader(random_title)
st.write(random_thought)
