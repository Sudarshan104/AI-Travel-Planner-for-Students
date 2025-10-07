import streamlit as st
from google import generativeai as genai

# -------------------------
# Gemini Configuration
# -------------------------
GEMINI_API_KEY = "AIzaSyDzYcdKwdC6S8DpFHNS_-f47IQutxPKC5I"
genai.configure(api_key=GEMINI_API_KEY)
GEMINI_MODEL = "gemini-2.5-flash"

def generate_itinerary(destination, days, budget, interests):
    prompt = f"""
    Create a {days}-day travel itinerary for students visiting {destination}.
    Budget: {budget} USD
    Interests: {interests}
    Include daily activities, estimated costs, and travel tips.
    """
    response = genai.GenerativeModel(GEMINI_MODEL).generate_content(prompt)
    return response.text

# -------------------------
# Streamlit UI
# -------------------------
st.title("🎒 AI Travel Planner for Students")

destination = st.text_input("Destination city/country")
days = st.number_input("Number of days", min_value=1, max_value=30, value=3)
budget = st.number_input("Total budget (USD)", min_value=50, max_value=5000, value=500)
interests = st.text_input("Your interests (comma-separated, e.g., food, history, nature)")

if st.button("Generate Itinerary"):
    if destination and days and budget:
        st.info("Generating your personalized itinerary...")
        itinerary = generate_itinerary(destination, days, budget, interests)
        st.subheader("🗺️ Your AI-Generated Itinerary")
        st.write(itinerary)
        st.download_button("📥 Download Itinerary", itinerary, file_name="itinerary.txt")
    else:
        st.error("Please fill in all fields.")
