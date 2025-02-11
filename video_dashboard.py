import streamlit as st

st.set_page_config(page_title="AI Video Planner", layout="wide")

st.title("🎬 AI Video Planning Dashboard")
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", ["📅 Plan Content", "📝 Generate Script", "🎥 Create Video", "📊 Analytics"])

if page == "📅 Plan Content":
    st.subheader("📅 Plan Your Video Content")
elif page == "📝 Generate Script":
    st.subheader("📝 AI Script Generator")
elif page == "🎥 Create Video":
    st.subheader("🎥 Generate AI Video with HeyGen")
elif page == "📊 Analytics":
    st.subheader("📊 YouTube Video Analytics")

"📅 Plan Content"
import openai

st.subheader("📌 AI Video Idea Generator")
topic = st.text_input("Enter a keyword or topic:")
if st.button("🔍 Generate Video Ideas"):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": f"Generate 5 video ideas based on {topic}"}],
    )
    ideas = response["choices"][0]["message"]["content"]
    st.write("🎯 **AI Video Ideas:**")
    st.write(ideas)
