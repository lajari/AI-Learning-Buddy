
import streamlit as st
from google import genai
import os

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Learning Buddy")
st.caption("Your Personal AI Tutor powered by Gemini")

topic = st.text_input("Enter a Topic you want to learn")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."

        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"Create 5 MCQs on {topic} with answers."

        else:
            prompt = topic

        try:
          with st.spinner("🤖 Please wait... AI is preparing your lesson"):

            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )

            st.success("✅ Response Generated Successfully!")

            st.write(f"### 📚 Topic: {topic}")

            st.divider()

            st.markdown(response.text)

        except Exception as e:
            st.error(f"Error: {e}")

st.divider()
st.caption("Developed using Streamlit and Google Gemini API")
