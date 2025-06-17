import streamlit as st
import random

music_data = {
    "기쁨": {
        "한국 발라드": [
            ("볼빨간사춘기 – 여행", "https://www.youtube.com/watch?v=xRbPAVnqtcs"),
            ("아이유 – 너의 의미", "https://www.youtube.com/watch?v=ScSn235gQx0"),
            ("태연 – 사계", "https://www.youtube.com/watch?v=xwZhx40ke5s"),
        ]
    },
    "슬픔": {
        "한국 발라드": [
            ("김연우 – 여전히 아름다운지", "https://www.youtube.com/watch?v=rJkXU4YyQ5w"),
            ("정승환 – 너였다면", "https://www.youtube.com/watch?v=K6g2ToX6lRg"),
            ("백예린 – 다시 난, 여기", "https://www.youtube.com/watch?v=OEZP0KsTCHg"),
        ]
    },
    "화남": {
        "힙합": [
            ("ASH ISLAND – 악몽", "https://www.youtube.com/watch?v=9n61n0nLg2g"),
            ("버즈 – 남자를 몰라", "https://www.youtube.com/watch?v=vY4ov2dchQY"),
            ("빈지노 – Break", "https://www.youtube.com/watch?v=msK8NqlM-2k"),
        ]
    },
    "평온": {
        "인디": [
            ("성시경 – 우린 제법 잘 어울려요", "https://www.youtube.com/watch?v=tOqFVzWPOZ4"),
            ("잔나비 – 주저하는 연인들을 위해", "https://www.youtube.com/watch?v=NsRKoOIwZ5k"),
            ("윤딴딴 – 내 마음에", "https://www.youtube.com/watch?v=UbDU3Ub6RG8"),
        ]
    },
    "불안": {
        "발라드": [
            ("나윤권 – 나였으면", "https://www.youtube.com/watch?v=InVFHb3nYdw"),
            ("김연우 – 이 밤이 지나면", "https://www.youtube.com/watch?v=XBbK7r-FfHo"),
            ("적재 – 별 보러 가자", "https://www.youtube.com/watch?v=Z8r9iZhDYrQ"),
        ]
    },
    "설렘": {
        "한국 발라드": [
            ("볼빨간사춘기 – 나의 사춘기에게", "https://www.youtube.com/watch?v=U7RzTR5fV3s"),
            ("마크툽 – Marry Me", "https://www.youtube.com/watch?v=NGn15v9oZ9c"),
            ("이하이 – 한숨", "https://www.youtube.com/watch?v=l-xT0z7jNVY"),
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

if st.button("🎧 추천 음악 보기"):
    rec = []
    for genre_songs in music_data[emotion].values():
        rec.extend(random.sample(genre_songs, min(2, len(genre_songs))))
    st.session_state.recommended = rec

if st.session_state.recommended:
    st.subheader("🎵 추천 곡 리스트:")
    for title, url in st.session_state.recommended:
        st.markdown(f"**{title}**")
        st.video(url)
