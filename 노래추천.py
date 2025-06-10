import streamlit as st
import random

# 감정별 음악 추천 데이터
music_data = {
    "기쁨": [
        ("Happy - Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
        ("Can't Stop The Feeling! - Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw"),
        ("Uptown Funk - Bruno Mars", "https://www.youtube.com/watch?v=OPf0YbXqDm0"),
        ("Best Day Of My Life - American Authors", "https://www.youtube.com/watch?v=Y66j_BUCBMY")
    ],
    "슬픔": [
        ("Someone Like You - Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
        ("Let Her Go - Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA"),
        ("Lost Stars - Adam Levine", "https://www.youtube.com/watch?v=cL4uhaQ58Rk"),
        ("Jealous - Labrinth", "https://www.youtube.com/watch?v=50VWOBi0VFs")
    ],
    "화남": [
        ("In The End - Linkin Park", "https://www.youtube.com/watch?v=eVTXPUF4Oz4"),
        ("Stronger - Kanye West", "https://www.youtube.com/watch?v=PsO6ZnUZI0g"),
        ("Smells Like Teen Spirit - Nirvana", "https://www.youtube.com/watch?v=hTWKbfoikeg"),
        ("Breaking the Habit - Linkin Park", "https://www.youtube.com/watch?v=v2H4l9RpkwM")
    ],
    "평온": [
        ("Weightless - Marconi Union", "https://www.youtube.com/watch?v=UfcAVejslrU"),
        ("River Flows in You - Yiruma", "https://www.youtube.com/watch?v=7maJOI3QMu0"),
        ("Sunset Lover - Petit Biscuit", "https://www.youtube.com/watch?v=wJkKzZ8jU7s"),
        ("Bloom - The Paper Kites", "https://www.youtube.com/watch?v=8inJtTG_DuU")
    ]
}

# 감정별 배경 색상 (그라데이션 포함)
backgrounds = {
    "기쁨": "linear-gradient(135deg, #f6d365 0%, #fda085 100%)",
    "슬픔": "linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%)",
    "화남": "linear-gradient(135deg, #f77062 0%, #fe5196 100%)",
    "평온": "linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%)"
}

# 감정 선택
st.set_page_config(page_title="감정 기반 음악 추천기", layout="wide")
emotion = st.selectbox("🎭 지금 기분은 어떤가요?", list(music_data.keys()))

# 배경 변경을 위한 스타일 삽입
st.markdown(f"""
    <style>
    .stApp {{
        background: {backgrounds[emotion]};
        background-attachment: fixed;
        color: white;
    }}
    .recommend-box {{
        background-color: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        margin-bottom: 1rem;
        border-radius: 1rem;
    }}
    a {{
        color: #ffffff;
        font-weight: bold;
        text-decoration: underline;
    }}
    </style>
""", unsafe_allow_html=True)

st.title("🎵 감정 기반 음악 추천기")
st.markdown("당신의 감정에 어울리는 음악 3곡을 추천해드릴게요.")

# 추천 버튼
if st.button("🎧 추천 음악 보기"):
    st.subheader(f"🎶 {emotion}한 기분에 어울리는 음악들:")
    songs = random.sample(music_data[emotion], 3)
    for title, url in songs:
        st.markdown(f'<div class="recommend-box">🎵 <a href="{url}" target="_blank">{title}</a></div>', unsafe_allow_html=True)
