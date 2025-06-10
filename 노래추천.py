import streamlit as st
import random

# --- 감정별 > 장르별 음악 데이터 (장르 1개씩 추가, 곡도 2곡씩 추가) ---
music_data = {
    "기쁨": {
        "한국 발라드": [
            ("행복한 하루 - 아이유", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
            ("기분 좋은 날 - 백현", "https://www.youtube.com/watch?v=ru0K8uYEZWw"),
        ],
        "해외 팝송": [
            ("Happy - Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
            ("Can't Stop The Feeling! - Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw"),
        ],
        "댄스": [
            ("Uptown Funk - Bruno Mars", "https://www.youtube.com/watch?v=OPf0YbXqDm0"),
            ("Good Time - Owl City & Carly Rae Jepsen", "https://www.youtube.com/watch?v=H7HmzwI67ec"),
        ],
    },
    "슬픔": {
        "한국 발라드": [
            ("너를 만나 - 폴킴", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
            ("사랑했지만 - 김광석", "https://www.youtube.com/watch?v=RBumgq5yVrA"),
        ],
        "해외 팝송": [
            ("Someone Like You - Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
            ("Let Her Go - Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA"),
        ],
        "재즈": [
            ("What a Wonderful World - Louis Armstrong", "https://www.youtube.com/watch?v=CWzrABouyeE"),
            ("My Funny Valentine - Chet Baker", "https://www.youtube.com/watch?v=UZJk2VbCMj0"),
        ],
    },
    "화남": {
        "락": [
            ("In The End - Linkin Park", "https://www.youtube.com/watch?v=eVTXPUF4Oz4"),
            ("Smells Like Teen Spirit - Nirvana", "https://www.youtube.com/watch?v=hTWKbfoikeg"),
        ],
        "힙합": [
            ("Stronger - Kanye West", "https://www.youtube.com/watch?v=PsO6ZnUZI0g"),
            ("Break Stuff - Limp Bizkit", "https://www.youtube.com/watch?v=ZpUYjpKg9KY"),
        ],
        "펑크": [
            ("American Idiot - Green Day", "https://www.youtube.com/watch?v=Ee_uujKuJMI"),
            ("Holiday - Green Day", "https://www.youtube.com/watch?v=8VG7xj6vJTo"),
        ],
    },
    "평온": {
        "클래식": [
            ("Weightless - Marconi Union", "https://www.youtube.com/watch?v=UfcAVejslrU"),
            ("River Flows in You - Yiruma", "https://www.youtube.com/watch?v=7maJOI3QMu0"),
        ],
        "일렉트로닉": [
            ("Sunset Lover - Petit Biscuit", "https://www.youtube.com/watch?v=wJkKzZ8jU7s"),
            ("A Moment Apart - ODESZA", "https://www.youtube.com/watch?v=hv44srAsAo4"),
        ],
        "포크": [
            ("Skinny Love - Bon Iver", "https://www.youtube.com/watch?v=ssdgFoHLwnk"),
            ("Bloom - The Paper Kites", "https://www.youtube.com/watch?v=4umIW3rZs1Y"),
        ],
    },
    "불안": {
        "팝": [
            ("Lovely - Billie Eilish & Khalid", "https://www.youtube.com/watch?v=V1Pl8CzNzCw"),
            ("Breathe Me - Sia", "https://www.youtube.com/watch?v=wbH3yCtU3tE"),
        ],
        "인디": [
            ("Je te laisserai des mots - Patrick Watson", "https://www.youtube.com/watch?v=CLiXUT3MS34"),
            ("Asleep - The Smiths", "https://www.youtube.com/watch?v=VjEq-r2agqc"),
        ],
        "알앤비": [
            ("Earned It - The Weeknd", "https://www.youtube.com/watch?v=WLnwsA7Ksas"),
            ("Location - Khalid", "https://www.youtube.com/watch?v=by3yNv8i8gk"),
        ],
    },
    "설렘": {
        "팝": [
            ("I Really Like You - Carly Rae Jepsen", "https://www.youtube.com/watch?v=qV5lzRHrGeg"),
            ("Electric Love - BØRNS", "https://www.youtube.com/watch?v=RYr96YYEaZY"),
        ],
        "록": [
            ("Lover - Taylor Swift", "https://www.youtube.com/watch?v=-BjZmE2gtdo"),
            ("Adore You - Harry Styles", "https://www.youtube.com/watch?v=VF-r5TtlT9w"),
        ],
        "인디 팝": [
            ("Dog Days Are Over - Florence + The Machine", "https://www.youtube.com/watch?v=iWOyfLBYtuU"),
            ("Pumped Up Kicks - Foster The People", "https://www.youtube.com/watch?v=SDTZ7iX4vTQ"),
        ],
    },
}

background_colors = {
    "기쁨": "#FFE082",
    "슬픔": "#90CAF9",
    "화남": "#EF9A9A",
    "평온": "#A5D6A7",
    "불안": "#CE93D8",
    "설렘": "#F8BBD0",
}

quotes = {
    "기쁨": "기쁨은 삶의 향기입니다. – 헬렌 켈러",
    "슬픔": "눈물은 마음의 언어입니다.",
    "화남": "화를 다스리는 것이 진정한 힘이다. – 달라이 라마",
    "평온": "평온은 내면에서 시작된다.",
    "불안": "불안은 내일 걱정에 시간을 낭비하는 것이다.",
    "설렘": "설렘은 새로운 시작의 신호입니다.",
}

if "recommended" not in st.session_state:
    st.session_state.recommended = []

st.set_page_config(page_title="감정 기반 음악 추천기", layout="wide")

# 감정 선택
emotion = st.selectbox("🎭 지금 기분은 어떤가요?", list(music_data.keys()))

# 배경색 적용
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {background_colors[emotion]};
    }}
    </style>
""", unsafe_allow_html=True)

# 감정별 명언 출력
st.markdown(f"### 💬 {quotes[emotion]}")

# 장르 선택 (복수 선택 가능)
genres = list(music_data[emotion].keys())
selected_genres = st.multiselect("🎶 장르를 선택하세요 (최소 1개)", genres, default=genres)

st.title("🎵 감정 기반 음악 추천기")
st.markdown("당신의 감정에 어울리는 음악을 추천해드릴게요! (각 장르별 2곡씩)")

if st.button("🎧 추천 음악 보기"):
    recommended_songs = []
    for genre in selected_genres:
        songs = music_data[emotion][genre]
        count = min(2, len(songs))
        recommended_songs.extend(random.sample(songs, count))
    st.session_state.recommended = recommended_songs

if st.session_state.recommended:
    st.subheader(f"🎶 {emotion}한 기분에 어울리는 음악 추천:")
    for title, url in st.session_state.recommended:
        st.markdown(f"**{title}**")
        st.video(url)
