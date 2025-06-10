import streamlit as st
import random

# --- 감정별 음악 데이터 ---
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

# --- 감정별 배경 테마 ---
backgrounds = {
    "기쁨": "linear-gradient(135deg, #f6d365 0%, #fda085 100%)",
    "슬픔": "linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%)",
    "화남": "linear-gradient(135deg, #f77062 0%, #fe5196 100%)",
    "평온": "linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%)"
}

# --- 페이지 설정 ---
st.set_page_config(page_title="감정 기반 음악 추천기", layout="wide")

# --- 세션 상태 초기화 ---
if "liked_songs" not in st.session_state:
    st.session_state.liked_songs = []
if "recommended" not in st.session_state:
    st.session_state.recommended = []

# --- 감정 선택 ---
emotion = st.selectbox("🎭 지금 기분은 어떤가요?", list(music_data.keys()))

# --- 동적 배경 ---
st.markdown(f"""
    <style>
    .stApp {{
        background: {backgrounds[emotion]};
        background-attachment: fixed;
        color: white;
    }}
    .song-box {{
        background-color: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        margin-bottom: 1rem;
        border-radius: 1rem;
    }}
    </style>
""", unsafe_allow_html=True)

st.title("🎵 감정 기반 음악 추천기")
st.markdown("당신의 감정에 어울리는 음악을 추천하고 저장해드릴게요!")

# --- 추천 버튼 ---
if st.button("🎧 추천 음악 보기"):
    st.session_state.recommended = random.sample(music_data[emotion], 3)

# --- 음악 추천 표시 ---
if st.session_state.recommended:
    st.subheader(f"🎶 {emotion}한 기분에 어울리는 음악:")
    for title, url in st.session_state.recommended:
        with st.container():
            st.markdown(f'<div class="song-box"><b>{title}</b></div>', unsafe_allow_html=True)
            st.video(url)
            if st.button(f"❤️ {title}", key=title):
                st.session_state.liked_songs.append((title, url))
                st.success(f"'{title}' 을(를) 좋아요에 저장했어요!")

# --- 저장된 노래 목록 ---
if st.session_state.liked_songs:
    with st.expander("📌 내가 좋아요 한 음악 보기"):
        for title, url in st.session_state.liked_songs:
            st.markdown(f"🎵 [{title}]({url})")

# --- 초기화 버튼 ---
if st.button("🔄 추천 & 좋아요 초기화"):
    st.session_state.recommended = []
    st.session_state.liked_songs = []
    st.warning("모든 추천과 좋아요가 초기화되었습니다.")
