import streamlit as st
import random

# --- 감정별 음악 데이터 ---
music_data = {
    "기쁨": [
        ("Happy - Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
        ("Can't Stop The Feeling! - Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw"),
        ("Uptown Funk - Bruno Mars", "https://www.youtube.com/watch?v=OPf0YbXqDm0"),
    ],
    "슬픔": [
        ("Someone Like You - Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
        ("Let Her Go - Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA"),
        ("Lost Stars - Adam Levine", "https://www.youtube.com/watch?v=cL4uhaQ58Rk"),
    ],
    "화남": [
        ("In The End - Linkin Park", "https://www.youtube.com/watch?v=eVTXPUF4Oz4"),
        ("Stronger - Kanye West", "https://www.youtube.com/watch?v=PsO6ZnUZI0g"),
        ("Smells Like Teen Spirit - Nirvana", "https://www.youtube.com/watch?v=hTWKbfoikeg"),
    ],
    "평온": [
        ("Weightless - Marconi Union", "https://www.youtube.com/watch?v=UfcAVejslrU"),
        ("River Flows in You - Yiruma", "https://www.youtube.com/watch?v=7maJOI3QMu0"),
        ("Sunset Lover - Petit Biscuit", "https://www.youtube.com/watch?v=wJkKzZ8jU7s"),
    ]
}

# --- 감정별 배경 색상 ---
background_colors = {
    "기쁨": "#FFE082",  # 밝은 노랑
    "슬픔": "#90CAF9",  # 연한 파랑
    "화남": "#EF9A9A",  # 연한 빨강
    "평온": "#A5D6A7",  # 연한 초록
}

# --- 세션 상태 초기화 ---
if "liked_songs" not in st.session_state:
    st.session_state.liked_songs = []
if "recommended" not in st.session_state:
    st.session_state.recommended = []

# --- 페이지 설정 ---
st.set_page_config(page_title="감정 기반 음악 추천기", layout="wide")

# --- 감정 선택 ---
emotion = st.selectbox("🎭 지금 기분은 어떤가요?", list(music_data.keys()))

# --- 배경 색상 적용 (단색) ---
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {background_colors[emotion]};
    }}
    </style>
""", unsafe_allow_html=True)

# --- 제목 ---
st.title("🎵 감정 기반 음악 추천기")
st.markdown("당신의 감정에 어울리는 음악을 추천해드릴게요!")

# --- 추천 버튼 ---
if st.button("🎧 추천 음악 보기"):
    st.session_state.recommended = random.sample(music_data[emotion], 3)

# --- 추천 곡 표시 ---
if st.session_state.recommended:
    st.subheader(f"🎶 {emotion}한 기분에 어울리는 음악:")
    for title, url in st.session_state.recommended:
        st.markdown(f"**{title}**")
        st.video(url)
        if st.button(f"❤️ 좋아요: {title}", key=title):
            if (title, url) not in st.session_state.liked_songs:
                st.session_state.liked_songs.append((title, url))
                st.success(f"'{title}'을(를) 좋아요에 저장했어요!")

# --- 저장된 곡 목록 ---
if st.session_state.liked_songs:
    with st.expander("📌 내가 좋아요 한 음악 보기"):
        for title, url in st.session_state.liked_songs:
            st.markdown(f"🎵 [{title}]({url})")

# --- 초기화 버튼 ---
if st.button("🔄 초기화"):
    st.session_state.recommended = []
    st.session_state.liked_songs = []
    st.warning("추천과 좋아요가 모두 초기화되었습니다.")
