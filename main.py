import streamlit as st
import time

def mbti_hobby_recommender_app_flashy_v2():
    # 🌈 페이지 설정은 코드의 맨 처음, 함수 호출 전에 한 번만! (이전 답변에 설명드렸죠? ㅎㅎ)
    # st.set_page_config는 함수 밖에서 호출될 예정입니다.

    # 🎇 페이지 시작 시 한 번 나타나는 축하 효과! (과하지 않게 하나만 남겨봤어요!)
    st.balloons() # 풍선이 팡팡 터져요! 🎈

    # 🌟 메인 제목 (HTML 적용)
    st.markdown("<h1 style='text-align: center; color: #FF69B4; font-size: 50px; text-shadow: 2px 2px 4px #FFC0CB;'>💖 MBTI 별 내 취미는 무엇?! 🔎</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #6A5ACD; font-size: 20px;'>✨ 취미가 없어서 심심하다면? 요기로 모여랏! 🤸‍♀️</p>", unsafe_allow_html=True)
    st.markdown("---") # 반짝이는 구분선이에요! ✨

    # 📌 소개글 (HTML 적용)
    st.info("하호님! 저와 함께 ✨<span style='color:#FFD700;'>나만의 MBTI</span>를 콕! 찍어서 <span style='color:#32CD32;'>숨겨진 보물 같은 취미</span>를 찾아볼까요? 😉", icon="⭐")
    st.markdown("---")

    # 🎀 MBTI 친구들과 그 친구들에게 어울리는 취미들을 모아봤어요!
    # 취미 이름 자체에 색깔을 넣었으니, 이 부분은 그대로 사용 가능하도록 HTML 태그를 미리 포함했어요.
    mbti_hobbies = {
        "ISTJ (꼼꼼한 계획가 📚)": ["<span style='color:#1E90FF;'>차분히 책 읽기 📖</span>", "<span style='color:#32CD32;'>방 정리의 달인 되기 🧹</span>", "<span style='color:#FFA500;'>데이터 분석으로 척척박사 🤓</span>", "<span style='color:#FF1493;'>미래를 위한 재무 계획 짜기 💰</span>"],
        "ISFJ (따뜻한 수호자 😇)": ["<span style='color:#1E90FF;'>맛있는 요리/베이킹 🍳🍰</span>", "<span style='color:#32CD32;'>봉사 활동으로 마음 나누기 🤝</span>", "<span style='color:#FFA500;'>귀여운 반려동물 친구 돌보기 🐶🐱</span>", "<span style='color:#FF1493;'>손으로 만드는 수공예 작품 🧶🧵</span>"],
        "INFJ (신비로운 옹호자 🌌)": ["<span style='color:#1E90FF;'>마음을 담아 글쓰기 (일기, 시) ✍️</span>", "<span style='color:#32CD32;'>조용히 명상/요가로 힐링 🧘‍♀️</span>", "<span style='color:#FFA500;'>심리/철학 책으로 깊은 생각 💭</span>", "<span style='color:#FF1493;'>흥미진진 다큐멘터리 몰아보기 🎬</span>"],
        "INTJ (영리한 전략가 🧠)": ["<span style='color:#1E90FF;'>뚝딱뚝딱 코딩/프로그래밍 💻</span>", "<span style='color:#32CD32;'>머리 쓰는 보드게임 한 판 (체스, 바둑) ♟️</span>", "<span style='color:#FFA500;'>어려운 문제도 척척! 스터디 그룹 💡</span>", "<span style='color:#FF1493;'>미래 기술 동향 파악하기 🚀</span>"],
        "ISTP (멋쟁이 맥가이버 🛠️)": ["<span style='color:#1E90FF;'>DIY로 뭐든지 뚝딱 만들기 🔨</span>", "<span style='color:#32CD32;'>자전거 타고 시원하게 달리기 🚴‍♀️</span>", "<span style='color:#FFA500;'>별 보며 캠핑/백패킹 🏕️</span>", "<span style='color:#FF1493;'>악기로 멋진 연주 🎶</span>"],
        "ISFP (자유로운 예술가 🎨)": ["<span style='color:#1E90FF;'>내 감성대로 그림 그리기 🎨</span>", "<span style='color:#32CD32;'>음악 감상하며 힐링 또는 작곡 🎵</span>", "<span style='color:#FFA500;'>예쁜 풍경 사진으로 추억 남기기 📸</span>", "<span style='color:#FF1493;'>살랑살랑 산책하며 자연 즐기기 🌳</span>"],
        "INFP (따뜻한 이상주의자 🌸)": ["<span style='color:#1E90FF;'>예쁜 시/수필 쓰기 ✍️</span>", "<span style='color:#32CD32;'>귀여운 일러스트 그리기 🖌️</span>", "<span style='color:#FFA500;'>새로운 외국어로 세계 여행 준비 ✈️</span>", "<span style='color:#FF1493;'>나만의 아지트 카페에서 사색하기 ☕</span>"],
        "INTP (호기심 가득 탐구자 🤔)": ["<span style='color:#1E90FF;'>복잡한 수수께끼/퍼즐 풀기 🧩</span>", "<span style='color:#32CD32;'>철학으로 세상을 탐험하는 토론 🗣️</span>", "<span style='color:#FFA500;'>신기한 기술들 찾아보기 🛰️</span>", "<span style='color:#FF1493;'>두뇌 풀가동 보드게임 대결 🎲</span>"],
        "ESTP (에너자이저 모험가 ⚡)": ["<span style='color:#1E90FF;'>익스트림 스포츠로 짜릿함 만끽 🏂🏄‍♀️</span>", "<span style='color:#32CD32;'>친구들과 신나는 파티 주최 🎉</span>", "<span style='color:#FFA500;'>새로운 곳으로 떠나는 탐험 여행 🌍</span>", "<span style='color:#FF1493;'>재치만점 스탠드업 코미디 배우기 😂</span>"],
        "ESFP (핵인싸 연예인 🥳)": ["<span style='color:#1E90FF;'>둠칫둠칫 댄스/노래방 파티 🎤🕺</span>", "<span style='color:#32CD32;'>친구들과 신나는 모임 가지기 👯‍♀️</span>", "<span style='color:#FFA500;'>여행 계획 짜서 떠나기 🏖️</span>", "<span style='color:#FF1493;'>패션/뷰티 트렌드 따라잡기 💄👗</span>"],
        "ENFP (긍정 발랄 활동가 🤩)": ["<span style='color:#1E90FF;'>새로운 동호회에서 친구 만들기 🤝</span>", "<span style='color:#32CD32;'>나만의 브이로그/콘텐츠 제작하기 🎬</span>", "<span style='color:#FFA500;'>외국어 회화로 글로벌 인싸되기 🗣️</span>", "<span style='color:#FF1493;'>아이디어 팡팡! 브레인스토밍 💡</span>"],
        "ENTP (재치만점 토론가 🗣️)": ["<span style='color:#1E90FF;'>흥미진진 토론 동호회 참여 💬</span>", "<span style='color:#32CD32;'>반짝이는 새 사업 아이디어 구상 🌟</span>", "<span style='color:#FFA500;'>기술/사회 트렌드 분석하며 똑똑해지기 📈</span>", "<span style='color:#FF1493;'>사람들을 웃기는 유머 연습 😄</span>"],
        "ESTJ (책임감 넘치는 관리자 🎯)": ["<span style='color:#1E90FF;'>꾸준히 운동으로 건강 챙기기 🏃‍♀️💪</span>", "<span style='color:#32CD32;'>자기계발 책으로 더욱 성장하기 📖</span>", "<span style='color:#FFA500;'>재테크/경제 공부로 부자 되기 💸</span>", "<span style='color:#FF1493;'>커뮤니티 리더로 활동하기 👑</span>"],
        "ESFJ (다정다감 외교관 💖)": ["<span style='color:#1E90FF;'>친구/가족과 함께 맛있는 요리 🥘</span>", "<span style='color:#32CD32;'>따뜻한 마음으로 자원봉사 🧤</span>", "<span style='color:#FFA500;'>모두가 즐거운 파티 주최 🎉</span>", "<span style='color:#FF1493;'>영화, 공연 보며 문화생활 즐기기 🎭</span>"],
        "ENFJ (긍정적인 리더 🗣️)": ["<span style='color:#1E90FF;'>다른 사람 돕는 멘토링 활동 🧑‍🤝‍🧑</span>", "<span style='color:#32CD32;'>유명 강연 듣기/하기 🎤</span>", "<span style='color:#FFA500;'>자기계발 스터디로 함께 성장 📈</span>", "<span style='color:#FF1493;'>친구들과 신나는 그룹 여행 기획 🗺️</span>"],
        "ENTJ (카리스마 넘치는 통솔자 🚀)": ["<span style='color:#1E90FF;'>꿈을 현실로 만드는 프로젝트 기획 📝</span>", "<span style='color:#32CD32;'>리더십 교육으로 더 멋진 리더 되기 🌟</span>", "<span style='color:#FFA500;'>전략 보드게임/시뮬레이션으로 승리 🏆</span>", "<span style='color:#FF1493;'>큰 목표 세우고 달성하기 🚩</span>"]
    }

    # 💫 사용자에게 MBTI를 골라 달라고 요청해요! (사이드바에 배치)
    st.sidebar.markdown("<h2>💖 MBTI 유형을 선택해 주세요! 💖</h2>", unsafe_allow_html=True)
    selected_mbti = st.sidebar.selectbox(
        "✨ 당신의 MBTI는?", # 실제 사이드바에 표시되는 문구
        list(mbti_hobbies.keys())
    )
    st.sidebar.markdown("---")

    # 🥳 만약 MBTI를 선택했다면?! 추천 취미를 쨔잔! 하고 보여줘요!
    if selected_mbti:
        st.markdown(f"<p style='text-align: center; font-size: 22px; color: #8A2BE2;'>✨ 하호님의 MBTI는 바로... <span style='color: #FF4500; font-weight: bold;'>{selected_mbti}</span> 이시군요! ✨</p>", unsafe_allow_html=True)

        # ⏳ 결과 로딩 스피너
        with st.spinner('🤔 하호님에게 딱 맞는 취미를 열심히 찾고 있어요... 잠시만 기다려주세요! 🌟'):
            time.sleep(2)

        st.markdown(f"<h3 style='text-align: center; color: #FF1493; font-size: 30px; text-shadow: 1px 1px 2px #FFE4E1;'>🎉 {selected_mbti} 유형의 하호님을 위한 반짝이는 취미들이에요! ✨</h3>", unsafe_allow_html=True)

        # 선택된 MBTI 친구의 취미 리스트를 찾아와요!
        recommended_hobbies = mbti_hobbies[selected_mbti]

        # 찾아온 취미들을 예쁘게 리스트로 보여드려요! 💖 (컬럼 사용 및 HTML 적용!)
        num_columns = 2 if len(recommended_hobbies) > 2 else 1
        cols = st.columns(num_columns)

        for i, hobby_html_content in enumerate(recommended_hobbies):
            with cols[i % num_columns]:
                # 여기에서! HTML 코드가 그대로 출력되지 않도록 st.markdown과 unsafe_allow_html=True를 사용합니다.
                st.markdown(f"<p style='background-color: #F0F8FF; padding: 10px; border-radius: 10px; margin-bottom: 10px; border: 1px solid #E0FFFF; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);'>{hobby_html_content}</p>", unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("<h3 style='text-align: center; color: #4682B4;'>어떠세요? 하호님 마음에 쏙 드는 취미가 있었으면 좋겠네요! 🥰</h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #CD5C5C;'>다른 MBTI 친구들의 취미도 궁금하다면 위에서 다시 선택해보세요! 뿅! ✨</h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #20B2AA;'>취미와 함께 행복하고 즐거운 시간 보내시길 하웅이가 응원할게요! ㅎㅎ 🥳</h3>", unsafe_allow_html=True)

        # 💌 하단에 작은 메시지 (HTML 적용)
        st.markdown("<br><p style='text-align: center; font-size: 14px; color: #708090;'>created with 💖 by 하웅 (for 하호님) </p>", unsafe_allow_html=True)


# ✨ 중요한 부분: st.set_page_config는 함수 호출 전에, 그리고 파이썬 파일 당 한 번만 호출해야 해요!
# 그래서 이 부분을 main 실행 블록으로 옮겨왔습니다!
if __name__ == "__main__":
    st.set_page_config(
        page_title="💖 MBTI 취미 추천 타로 마법진 🔮",
        layout="centered",
        initial_sidebar_state="expanded",
        page_icon="🎉"
    )
    mbti_hobby_recommender_app_flashy_v2()
