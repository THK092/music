import streamlit as st
import random

# 감정별 음악 추천 데이터
music_data = {
    "기쁨": [
        ("Happy - Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
        ("Can't Stop The Feeling! - Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw"),
        ("Uptown Funk - Bruno Mars", "https://www.youtube.com/watch?v=OPf0YbXqDm0")
    ],
    "슬픔": [
        ("Someone Like You - Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
        ("Let Her Go - Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA"),
        ("Lost Stars - Adam Levine", "https://www.youtube.com/watch?v=cL4uhaQ58Rk")
    ],
    "화남": [
        ("In The End - Linkin Park", "https://www.youtube.com/watch?v=eVTXPUF4Oz4"),
        ("Stronger - Kanye West", "https://www.youtube.com/watch?v=PsO6ZnUZI0g"),
        ("Smells Like Teen Spirit - Nirvana", "https://www.youtube.com/watch?v=hTWKbfoikeg")
    ],
    "평온": [
        ("Weightless - Marconi Union", "https://www.youtube.com/watch?v=UfcAVejslrU"),
        ("River Flows in You - Yiruma", "https://www.youtube.com/watch?v=7maJOI3QMu0"),
        ("Sunset Lover - Petit Biscuit", "https://www.youtube.com/watch?v=wJkKzZ8jU7s")
    ]
}

# Streamlit UI
st.title("🎵 감정 기반 음악 추천기")
st.markdown("당신의 현재 감정을 선택하세요. 기분에 어울리는 음악을 추천해드릴게요!")

emotion = st.selectbox("지금 기분은 어떤가요?", list(music_data.keys()))

if st.button("음악 추천 받기"):
    song = random.choice(music_data[emotion])
    st.success(f"🎧 추천곡: [{song[0]}]({song[1]})")
