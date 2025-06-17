import streamlit as st
import random

# 감정별 > 장르별 > 노래 제목과 유튜브 링크
music_data = {
    "기쁨": {
        "한국 발라드": [
            ("아이유 – 너의 의미", "https://www.youtube.com/watch?v=ScSn235gQx0"),
            ("볼빨간사춘기 – 여행", "https://www.youtube.com/watch?v=xRbPAVnqtcs"),
        ]
    },
    "슬픔": {
        "한국 발라드": [
            ("김연우 – 여전히 아름다운지", "https://www.youtube.com/watch?v=rJkXU4YyQ5w"),
            ("정승환 – 너였다면", "https://www.youtube.com/watch?v=K6g2ToX6lRg"),
        ]
    },
    "화남": {
        "힙합": [
            ("ASH ISLAND – 악몽", "https://www.youtube.com/watch?v=9n61n0nLg2g"),
            ("버즈 – 남자를 몰라", "https://www.youtube.com/watch?v=vY4ov2dchQY"),
        ]
    },
    "평온": {
        "인디": [
            ("성시경 – 우린 제법 잘 어울려요", "https://www.youtube.com/watch?v=tOqFVzWPOZ4"),
            ("잔나비 – 주저하는 연인들을 위해", "https://www.youtube.com/watch?v=NsRKoOIwZ5k"),
        ]
    },
    "불안": {
        "발라드": [
            ("나윤권 – 나였으면", "https://www.youtube.com/watch?v=InVFHb3nYdw"),
            ("김연우 – 이 밤이 지나면", "https://www.youtube.com/watch?v=XBbK7r-FfHo"),
        ]
    },
    "설렘": {
        "한국 발라드": [
            ("볼빨간사춘기 – 나의 사춘기에게", "https://www.youtube.com/watch?v=U7RzTR5fV3s"),
            ("마크툽 – Marry Me", "https://www.youtube.com/watch?v=NGn15v9oZ9c"),
        ]
    },
}

background_colors = {
    "기쁨": "#FFF9C4",
    "슬픔": "#BBDEFB",
    "화남": "#FFCDD2",
    "평온": "#C8E6C9",
    "불안": "#E1BEE7",
    "설렘": "#F8BBD0",
}

st.set_page_config(page_title="감정 기반 음악 추천", layout="wide")

if "recommended" not in st.session_state:
    st.session_state.recommended = []

emotion = st.selectbox("😊 지금 기분은 어떤가요?", list(music_data.keys()))

# 배경색 적용
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {background_colors[emotion]};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

genres = list(music_data[emotion].keys())
selected_genres = st.multiselect("🎶 듣고 싶은 장르 선택", genres, default=genres)

if st.button("🎧 추천 음악 보기"):
    rec = []
    for genre in selected_genres:
        songs = music_data[emotion][genre]
        rec.extend(random.sample(songs, min(2, len(songs))))
    st.session_state.recommended = rec

if st.session_state.recommended:
    st.subheader("🎵 추천 곡 리스트:")
    for title, url in st.session_state.recommended:
        st.markdown(f"**{title}**")
        st.video(url)
