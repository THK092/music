import streamlit as st
import random

# --- 감정별 음악 데이터 ---
music_data = {
    "기쁨": [
        ("Happy - Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
        ("Can't Stop The Feeling! - Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw"),
        ("Uptown Funk - Bruno Mars", "https://www.youtube.com/watch?v=OPf0YbXqDm0"),
        ("Good Time - Owl City & Carly Rae Jepsen", "https://www.youtube.com/watch?v=H7HmzwI67ec"),
        ("Best Day Of My Life - American Authors", "https://www.youtube.com/watch?v=Y66j_BUCBMY"),
        ("Walking on Sunshine - Katrina & The Waves", "https://www.youtube.com/watch?v=iPUmE-tne5U"),
    ],
    "슬픔": [
        ("Someone Like You - Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
        ("Let Her Go - Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA"),
        ("Lost Stars - Adam Levine", "https://www.youtube.com/watch?v=cL4uhaQ58Rk"),
        ("When I Was Your Man - Bruno Mars", "https://www.youtube.com/watch?v=ekzHIouo8Q4"),
        ("All I Want - Kodaline", "https://www.youtube.com/watch?v=mtf7hC17IBM"),
        ("Fix You - Coldplay", "https://www.youtube.com/watch?v=k4V3Mo61fJM"),
    ],
    "화남": [
        ("In The End - Linkin Park", "https://www.youtube.com/watch?v=eVTXPUF4Oz4"),
        ("Stronger - Kanye West", "https://www.youtube.com/watch?v=PsO6ZnUZI0g"),
        ("Smells Like Teen Spirit - Nirvana", "https://www.youtube.com/watch?v=hTWKbfoikeg"),
        ("Break Stuff - Limp Bizkit", "https://www.youtube.com/watch?v=ZpUYjpKg9KY"),
        ("Numb - Linkin Park", "https://www.youtube.com/watch?v=kXYiU_JCYtU"),
        ("Fight Song - Rachel Platten", "https://www.youtube.com/watch?v=xo1VInw-SKc"),
    ],
    "평온": [
        ("Weightless - Marconi Union", "https://www.youtube.com/watch?v=UfcAVejslrU"),
        ("River Flows in You - Yiruma", "https://www.youtube.com/watch?v=7maJOI3QMu0"),
        ("Sunset Lover - Petit Biscuit", "https://www.youtube.com/watch?v=wJkKzZ8jU7s"),
        ("Bloom - ODESZA", "https://www.youtube.com/watch?v=5yk0w0sHb5g"),
        ("A Moment Apart - ODESZA", "https://www.youtube.com/watch?v=hv44srAsAo4"),
        ("Kiss the Rain - Yiruma", "https://www.youtube.com/watch?v=so6ExplQlaY"),
    ]
}

# --- 감정별 배경 색상 ---
background_colors = {
    "기쁨": "#FFE082",
    "슬픔": "#90CAF9",
    "화남": "#EF9A9A",
    "평온": "#A5D6A7",
}

# --- 세션 상태 초기화 ---
if "recommended" not in st.session_state:
    st.session_state.recommended = []

# --- 페이지 설정 ---
st.set_page_config(page_title="감정 기반 음악 추천기", layout="wide")

# --- 감정 선택 ---
emotion = st.selectbox("🎭 지금 기분은 어떤가요?", list(music_data.keys()))

# --- 배경 색상 적용 ---
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {background_colors[emotion]};
    }}
    </style>
""", unsafe_allow_html=True)

# --- 제목 ---
st.title("🎵 감정 기반 음악 추천기")
st.markdown("당신의 감정에 어울리는 음악 5곡을 추천해드릴게요!")

# --- 추천 버튼 ---
if st.button("🎧 추천 음악 보기"):
    st.session_state.recommended = random.sample(music_data[emotion], 5)

# --- 추천 곡 표시 ---
if st.session_state.recommended:
    st.subheader(f"🎶 {emotion}한 기분에 어울리는 음악 추천:")
    for title, url in st.session_state.recommended:
        st.markdown(f"**{title}**")
        st.video(url)
