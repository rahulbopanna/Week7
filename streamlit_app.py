import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
import os

st.title("Airline Experience Feedback")

# Prompt for user input on trip experience
user_experience = st.text_input("Share with us your experience of the latest trip:")

# Load API Key securely from Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OpenAIKey"]

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define the system prompt to classify and respond based on user feedback
if user_experience:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Analyze the user's feedback on their recent airline experience and respond accordingly. "
                                          "If they had a positive experience, thank them for their feedback. "
                                          "If they had a negative experience caused by the airline, offer sympathies and state that customer service will follow up. "
                                          "If the negative experience was beyond the airline's control, express sympathy and explain that the airline is not liable."},
            {"role": "user", "content": user_experience}
        ]
    )

    # Display the AI's response
    st.write(response.choices[0].message.content)
