import random
import streamlit as st

# Define the exercise lists

shoulder = {
    "kettlebell zercher and press": "https://youtube.com/shorts/rEmwZw2blqs?si=0_0Z1AcocynfUIDp",
    "kettlebell clean and press": "https://youtu.be/ExLymPrIhBQ?si=Jo7Lf2WUViZiEmhs",
    "kettlebell z press": "https://youtube.com/shorts/wto_8mVOHF8?si=M4jawG9Y9vyQgw7T",
    "pike push ups": "https://youtube.com/shorts/0cT6ug3WVn4?si=Sn-ey_fbTvF9V7-R",
    "kettlebell chops": "https://youtu.be/Psmkt_Tft5E?si=9gj8FZ-jFr9Vm_vs"
}
chest = {
    "kettlebell Floor press (lower)": "https://youtube.com/shorts/NHDQoqK8sXE?si=DfarH_cequPkzEAy", 
    "kettlebell crush grip press (both arms)": "https://youtu.be/A98BUB7jxU0?si=i4qAzDfWlrH7ktnQ", 
    "push ups (classic + diamond)": "https://youtu.be/XtU2VQVuLYs?si=hMQ9D8rmVR0h7bGI", 
    "kettlebell 90 degree floor press (upper)": "https://youtube.com/shorts/NHDQoqK8sXE?si=-Z40JVp1TFzgVVAH"
} 

back = {
    "pull ups": "https://youtube.com/shorts/gy1dyxEdCqc?si=zOhnMfPxsTinwdka", 
    "kettlebell rows": "https://youtube.com/shorts/xbtdGjYmrnM?si=8DnseOJ5Y3Cw8jm4", 
    "kettlebell snatch": "https://youtube.com/shorts/GV8kKDSprfQ?si=MthB8OqKVg699Yht", 
    "kettlebell snatchy lunges": "https://youtu.be/gqf0njGSiRI?si=xSyGmuRxQGnjZmW7", 
    "kettlebell pullover": "https://youtube.com/shorts/5dfA3OP4wx0?si=9byWzT8Qni-F-Sif"
}
legs = {
    "double kettlebell (one clean and one hanged) lunges": "https://youtube.com/shorts/V490qKi_Z8A?si=oKpxqarcD9vrfN-P", 
    "kang squat": "https://youtube.com/shorts/yF0zupwzg8E?si=qySTT1Ymfh7Mqyvi", 
    "kettlebell curtsy squat": "https://youtube.com/shorts/DpsNSe3VPYI?si=5iIznJ1_M3vZG7Bw", 
    "Romanian deadlift": "https://youtu.be/keiZFdUgvKQ?si=LyshBeXbCS9MoVSn", 
    "zercher squat": "https://youtube.com/shorts/xOwTaQdN2YY?si=1waZFb1k6SoF38Uy"
}
Full = {
    "kettlebell Overhead squat": "https://youtu.be/tpPKyhvf0IA?si=goat5wiTpUmq1TLE", 
    "thrusters": "https://youtube.com/shorts/Id0Qefh4AHc?si=xj6yu7Ud1xUsVlYj", 
    "kettlebell swing": "https://youtu.be/ae6nV6pFRG4?si=fpSZaDpJ8KpGaemZ", 
    "burpees": "https://youtu.be/G2hv_NYhM-A?si=PRLHbiTdIdpgWuc5", 
    "carry with lunges": "https://youtube.com/shorts/xQA8fZn1hzk?si=IjI6KWXad3KSdt3R"
}


# Function to generate a workout
def generate_workout(split):
    workout = []
    demos = []
    # if split = 'Push':
    return split
        

# Streamlit app layout
st.title("Kettlebell Workout Generator")
st.image('kb.jpg', caption='You Are Savage💪')
split = st.multiselect("What do you wanna perform ?", ["Chest", "Shoulder", "Back", "Legs", "Full Body"])
if st.button("Generate Your Savage Workout"):
    print(generate_workout(split))
    # st.info("Your Kettlebell Workout:")
    # for i, (exercise, demo) in enumerate(zip(workout, demos), start=1):
    #     with st.expander(f"Exercise {i}: {exercise}"):
    #         st.write("3x sets with 8-10x reps")
    #         st.link_button("How you can do it", demo)
