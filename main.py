import streamlit as st
from datetime import date
import random

def put_card(category, workout):
    today_date = date.today()
    today = today_date.strftime("%B %d, %Y")
    with st.expander(f"Date: {today}, {{category}}"):
        for work in workout:
            st.write(f":yellow[Exercise]: {work['exercise']} : :green[{work['sets']}] x :blue[{work['reps']}] ")
        
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

put_card(category = "Full Body", workout = [{"exercise": "Row to rotational clean to rotational press", "sets": 5, "reps": 6}, {"exercise": "Inchworm push ups to deadlift", "sets": 5, "reps": 10}, {"exercise": "Clean to Goblet Squats", "sets": 5, "reps": 5}])
