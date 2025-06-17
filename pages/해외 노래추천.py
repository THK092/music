import streamlit as st
import random

music_data = {
    "기쁨": {
        "팝송": [
            ("Pharrell Williams – Happy", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
            ("Katrina & The Waves – Walking on Sunshine", "https://www.youtube.com/watch?v=iPUmE-tne5U"),
        ]
    },
    "슬픔": {
        "팝송": [
            ("Lewis Capaldi – Someone You Loved", "https://www.youtube.com/watch?v=bCuhuePlP8o"),
            ("Billie Eilish – Everything I Wanted", "https://www.youtube.com/watch?v=EgBJmlPo8Xw"),
        ]
    },
    "화남": {
        "팝송": [
            ("Linkin Park – Numb", "https://www.youtube.com/watch?v=kXYiU_JCYtU"),
            ("Eminem – Lose Yourself", "https://www.youtube.com/watch?v=_Yhyp-_hX2s"),
        ]
    },
    "평온": {
        "팝송": [
            ("Coldplay – Yellow", "https://www.youtube.com/watch?v=yKNxeF4KMsY"),
            ("Ed Sheeran – Photograph", "https://www.youtube.com/watch?v=nSDgHBxUbVQ"),
        ]
    },
    "불안": {
        "팝송": [
            ("Radiohead – Creep", "https://www.youtube.com/watch?v=XFkzRNyygfk"),
            ("Sia – Breathe Me", "https://www.youtube.com/watch?v=wbP0cYw-Zrc"),
        ]
    },
    "설렘": {
        "팝송": [   
            ("Taylor Swift – Enchanted", "https://www.youtube.com/watch?v=YW3tjqvy2cg"),
            ("Shawn Mendes – Fallin’ All in You", "https://www.youtube.com/watch?v=8xg3vE8Ie_E"),
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
        if len(genre_songs) >= 2:
            rec.extend(random.sample(genre_songs, 2))
        else:
            rec.extend(genre_songs)
    st.session_state.recommended = rec

if st.session_state.recommended:
    st.subheader("🎵 추천 곡 리스트:")
    for title, url in st.session_state.recommended:
        st.markdown(f"**{title}**")
        try:
            st.video(url)
        except Exception as e:
            st.warning(f"동영상 불러오기 실패: {title}")
