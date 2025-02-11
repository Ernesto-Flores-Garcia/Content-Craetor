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
    messages=[{"role": "user", "content": user_input}]
    )

    ideas = response["choices"][0]["message"]["content"]
    st.write("🎯 **AI Video Ideas:**")
    st.write(ideas)

"📝 Generate Script"
st.subheader("📝 AI Script Generator")
video_topic = st.text_input("Enter Video Topic:")

if st.button("✍ Generate Script"):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": f"Write a YouTube video script about {video_topic}"}],
    )
    script = response["choices"][0]["message"]["content"]
    st.text_area("Generated Script:", script, height=250)

"🎥 Create Video"
import requests

st.subheader("🎥 Generate AI Video with HeyGen")
script = st.text_area("Enter the script for your video:")

if st.button("🎬 Generate Video"):
    heygen_payload = {
        "video_inputs": [{
            "character": {"type": "avatar", "avatar_id": "Brent_sitting_office_front"},
            "voice": {"type": "text", "voice_id": "26b2064088674c80b1e5fc5ab1a068ec", "input_text": script}
        }]
    }
    headers = {"Authorization": f"Bearer YOUR_HEYGEN_API_KEY"}
    response = requests.post("https://api.heygen.com/v1/video/generate", json=heygen_payload, headers=headers)

    if response.status_code == 200:
        video_id = response.json()["data"]["video_id"]
        st.success(f"✅ Video is processing! Video ID: {video_id}")
    else:
        st.error("❌ Error generating video")

"📊 Analytics"
from googleapiclient.discovery import build

st.subheader("📊 YouTube Video Analytics")
video_id = st.text_input("Enter YouTube Video ID:")

if st.button("📈 Get Analytics"):
    youtube = build("youtube", "v3", developerKey="YOUR_YOUTUBE_API_KEY")
    request = youtube.videos().list(part="statistics", id=video_id)
    response = request.execute()

    if "items" in response and response["items"]:
        stats = response["items"][0]["statistics"]
        st.write("📊 **Video Performance**")
        st.write(f"👍 Likes: {stats['likeCount']}")
        st.write(f"👀 Views: {stats['viewCount']}")
        st.write(f"💬 Comments: {stats['commentCount']}")
    else:
        st.error("❌ Video not found or API error")
