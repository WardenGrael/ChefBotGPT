import streamlit as st
import openai

# Initialize OpenAI API
openai.api_key = 'sk-proj-GTEszRZ7OJItQozU4DQ7T3BlbkFJkPiSRVNDByb17V7gS27a'

# Function to get meal plan from ChatGPT
def get_meal_plan(base_ingredients, servings):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that creates meal plans for workouts."},
        {"role": "user", "content": f"Create a detailed weekly meal plan for workouts using the following base ingredients: {base_ingredients}. Ensure each meal is designed for {servings} servings."}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message['content'].strip()

# Function to get water intake recommendation
def get_water_intake_recommendation(servings):
    daily_water_intake = 3.7 if servings > 1 else 2.7  # Rough estimate: use 3.7 liters for higher activity/multiple people, 2.7 liters otherwise
    return f"Based on your activity level and the number of servings, it's recommended to drink around {daily_water_intake} liters of water per day."

# Streamlit app layout
st.set_page_config(page_title="ChefGPT", layout="wide")

st.sidebar.title("ChefGPT")
st.sidebar.subheader("Want to make planning meals easier? Let ChefGPT do the work for you!")
base_ingredients = st.sidebar.text_area("What are your base ingredients? (Use Ctrl + Enter for new line)")
servings = st.sidebar.number_input("How many servings?", min_value=1, max_value=10, step=1)
submit_button = st.sidebar.button("Submit")

if submit_button:
    meal_plan = get_meal_plan(base_ingredients, servings)
    water_intake_recommendation = get_water_intake_recommendation(servings)
    st.markdown(f"### Weekly Meal Plan for {servings} Servings")
    st.markdown(meal_plan)
    st.markdown(f"### Daily Water Intake Recommendation")
    st.markdown(water_intake_recommendation)
else:
    st.markdown("### I'm ChefGPT! Here's a generated meal plan based on your inputed ingredients.")
    st.markdown("**Base Ingredients:** Your choice of ingredients")
    st.markdown("**Servings:** Number of servings you need")
    st.markdown("**Meal Plan:**")
    st.markdown("1. **Breakfast**")
    st.markdown("2. **Lunch**")
    st.markdown("3. **Dinner**")
    st.markdown("4. **Snacks**")

    st.markdown("Submit your ingredients and servings to get a personalized meal plan!")

