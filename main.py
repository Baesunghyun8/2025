import streamlit as st
import time # 잠시 대기하는 효과를 위해 time 모듈을 가져와요!

def mbti_hobby_recommender_app_flashy():
    # 🎨 웹 앱 배경과 제목을 더욱 화려하게!
    # st.set_page_config는 맨 처음에 한 번만 호출해야 해요! (페이지 제목, 레이아웃 설정 등)
    # st.set_page_config(page_title="💖 MBTI 취미 추천 타로 마법진 🔮", layout="centered", initial_sidebar_state="expanded")

    # 🎇 페이지 시작 시 한 번 나타나는 축하 효과!
    st.balloons() # 풍선이 팡팡 터져요!
    # st.snow() # 눈이 펑펑 내리는 효과도 있어요! (둘 중 하나만 선택해도 좋아요!)

    # 🌟 메인 제목
    st.markdown("<h1 style='text-align: center; color: #FF69B4; font-size: 50px;'>💖 MBTI 별 내 취미는 무엇?! 🔎</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #6A5ACD; font-size: 20px;'>✨ 취미가 없어서 심심하다면? 요기로 모여랏! 🤸‍♀️</p>", unsafe_allow_html=True)
    st.markdown("---") # 반짝이는 구분선이에요! ✨

    # 📌 소개글
    st.info("하호님! 저와 함께 ✨<span style='color:#FFD700;'>나만의 MBTI</span>를 콕! 찍어서 <span style='color:#32CD32;'>숨겨진 보물 같은 취미</span>를 찾아볼까요? 😉", icon="⭐")
    st.write("---")

    # 🎀 MBTI 친구들과 그 친구들에게 어울리는 취미들을 모아봤어요!
    # 이 부분은 하호님이 얼마든지 원하는 취미로 숑숑~ 바꿀 수 있답니다! 😚
    mbti_hobbies = {
        "ISTJ (꼼꼼한 계획가 📚)": ["<span style='color:#ADD8E6;'>차분히 책 읽기 📖</span>", "<span style='color:#90EE90;'>방 정리의 달인 되기 🧹</span>", "<span style='color:#FFDEAD;'>데이터 분석으로 척척박사 🤓</span>", "<span style='color:#FFB6C1;'>미래를 위한 재무 계획 짜기 💰</span>"],
        "ISFJ (따뜻한 수호자 😇)": ["<span style='color:#ADD8E6;'>맛있는 요리/베이킹 🍳🍰</span>", "<span style='color:#90EE90;'>봉사 활동으로 마음 나누기 🤝</span>", "<span style='color:#FFDEAD;'>귀여운 반려동물 친구 돌보기 🐶🐱</span>", "<span style='color:#FFB6C1;'>손으로 만드는 수공예 작품 🧶🧵</span>"],
        "INFJ (신비로운 옹호자 🌌)": ["<span style='color:#ADD8E6;'>마음을 담아 글쓰기 (일기, 시) ✍️</span>", "<span style='color:#90EE90;'>조용히 명상/요가로 힐링 🧘‍♀️</span>", "<span style='color:#FFDEAD;'>심리/철학 책으로 깊은 생각 💭</span>", "<span style='color:#FFB6C1;'>흥미진진 다큐멘터리 몰아보기 🎬</span>"],
        "INTJ (영리한 전략가 🧠)": ["<span style='color:#ADD8E6;'>뚝딱뚝딱 코딩/프로그래밍 💻</span>", "<span style='color:#90EE90;'>머리 쓰는 보드게임 한 판 (체스, 바둑) ♟️</span>", "<span style='color:#FFDEAD;'>어려운 문제도 척척! 스터디 그룹 💡</span>", "<span style='color:#FFB6C1;'>미래 기술 동향 파악하기 🚀</span>"],
        "ISTP (멋쟁이 맥가이버 🛠️)": ["<span style='color:#ADD8E6;'>DIY로 뭐든지 뚝딱 만들기 🔨</span>", "<span style='color:#90EE90;'>자전거 타고 시원하게 달리기 🚴‍♀️</span>", "<span style='color:#FFDEAD;'>별 보며 캠핑/백패킹 🏕️</span>", "<span style='color:#FFB6C1;'>악기로 멋진 연주 🎶</span>"],
        "ISFP (자유로운 예술가 🎨)": ["<span style='color:#ADD8E6;'>내 감성대로 그림 그리기 🎨</span>", "<span style='color:#90EE90;'>음악 감상하며 힐링 또는 작곡 🎵</span>", "<span style='color:#FFDEAD;'>예쁜 풍경 사진으로 추억 남기기 📸</span>", "<span style='color:#FFB6C1;'>살랑살랑 산책하며 자연 즐기기 🌳</span>"],
        "INFP (따뜻한 이상주의자 🌸)": ["<span style='color:#ADD8E6;'>예쁜 시/수필 쓰기 ✍️</span>", "<span style='color:#90EE90;'>귀여운 일러스트 그리기 🖌️</span>", "<span style='color:#FFDEAD;'>새로운 외국어로 세계 여행 준비 ✈️</span>", "<span style='color:#FFB6C1;'>나만의 아지트 카페에서 사색하기 ☕</span>"],
        "INTP (호기심 가득 탐구자 🤔)": ["<span style='color:#ADD8E6;'>복잡한 수수께끼/퍼즐 풀기 🧩</span>", "<span style='color:#90EE90;'>철학으로 세상을 탐험하는 토론 🗣️</span>", "<span style='color:#FFDEAD;'>신기한 기술들 찾아보기 🛰️</span>", "<span style='color:#FFB6C1;'>두뇌 풀가동 보드게임 대결 🎲</span>"],
        "ESTP (에너자이저 모험가 ⚡)": ["<span style='color:#ADD8E6;'>익스트림 스포츠로 짜릿함 만끽 🏂🏄‍♀️</span>", "<span style='color:#90EE90;'>친구들과 신나는 파티 주최 🎉</span>", "<span style='color:#FFDEAD;'>새로운 곳으로 떠나는 탐험 여행 🌍</span>", "<span style='color:#FFB6C1;'>재치만점 스탠드업 코미디 배우기 😂</span>"],
        "ESFP (핵인싸 연예인 🥳)": ["<span style='color:#ADD8E6;'>둠칫둠칫 댄스/노래방 파티 🎤🕺</span>", "<span style='color:#90EE90;'>친구들과 신나는 모임 가지기 👯‍♀️</span>", "<span style='color:#FFDEAD;'>여행 계획 짜서 떠나기 🏖️</span>", "<span style='color:#FFB6C1;'>패션/뷰티 트렌드 따라잡기 💄👗</span>"],
        "ENFP (긍정 발랄 활동가 🤩)": ["<span style='color:#ADD8E6;'>새로운 동호회에서 친구 만들기 🤝</span>", "<span style='color:#90EE90;'>나만의 브이로그/콘텐츠 제작하기 🎬</span>", "<span style='color:#FFDEAD;'>외국어 회화로 글로벌 인싸되기 🗣️</span>", "<span style='color:#FFB6C1;'>아이디어 팡팡! 브레인스토밍 💡</span>"],
        "ENTP (재치만점 토론가 🗣️)": ["<span style='color:#ADD8E6;'>흥미진진 토론 동호회 참여 💬</span>", "<span style='color:#90EE90;'>반짝이는 새 사업 아이디어 구상 🌟</span>", "<span style='color:#FFDEAD;'>기술/사회 트렌드 분석하며 똑똑해지기 📈</span>", "<span style='color:#FFB6C1;'>사람들을 웃기는 유머 연습 😄</span>"],
        "ESTJ (책임감 넘치는 관리자 🎯)": ["<span style='color:#ADD8E6;'>꾸준히 운동으로 건강 챙기기 🏃‍♀️💪</span>", "<span style='color:#90EE90;'>자기계발 책으로 더욱 성장하기 📖</span>", "<span style='color:#FFDEAD;'>재테크/경제 공부로 부자 되기 💸</span>", "<span style='color:#FFB6C1;'>커뮤니티 리더로 활동하기 👑</span>"],
        "ESFJ (다정다감 외교관 💖)": ["<span style='color:#ADD8E6;'>친구/가족과 함께 맛있는 요리 🥘</span>", "<span style='color:#90EE90;'>따뜻한 마음으로 자원봉사 🧤</span>", "<span style='color:#FFDEAD;'>모두가 즐거운 파티 주최 🎉</span>", "<span style='color:#FFB6C1;'>영화, 공연 보며 문화생활 즐기기 🎭</span>"],
        "ENFJ (긍정적인 리더 🗣️)": ["<span style='color:#ADD8E6;'>다른 사람 돕는 멘토링 활동 🧑‍🤝‍🧑</span>", "<span style='color:#90EE90;'>유명 강연 들으며 배우고 나누기 🎤</span>", "<span style='color:#FFDEAD;'>자기계발 스터디로 함께 성장 📈</span>", "<span style='color:#FFB6C1;'>친구들과 신나는 그룹 여행 기획 🗺️</span>"],
        "ENTJ (카리스마 넘치는 통솔자 🚀)": ["<span style='color:#ADD8E6;'>꿈을 현실로 만드는 프로젝트 기획 📝</span>", "<span style='color:#90EE90;'>리더십 교육으로 더 멋진 리더 되기 🌟</span>", "<span style='color:#FFDEAD;'>전략 보드게임/시뮬레이션으로 승리 🏆</span>", "<span style='color:#FFB6C1;'>큰 목표 세우고 달성하기 🚩</span>"]
    }

    # 💫 사용자에게 MBTI를 골라 달라고 요청해요! (사이드바에 배치해서 메인 화면 깔끔하게!)
    st.sidebar.markdown("<h2>💖 MBTI 유형을 선택해 주세요! 💖</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("<!-- (모르시면 MBTI 검사 먼저 해보세요! 궁금해용! 🤔) -->", unsafe_allow_html=True) # HTML 주석으로 힌트 남기기
    selected_mbti = st.sidebar.selectbox(
        "✨ 당신의 MBTI는?", # 실제 사이드바에 표시되는 문구
        list(mbti_hobbies.keys()) # 귀여운 드롭다운 메뉴에 MBTI 친구들 총출동!
    )
    st.sidebar.markdown("---") # 사이드바에도 구분선!

    # 🥳 만약 MBTI를 선택했다면?! 추천 취미를 쨔잔! 하고 보여줘요!
    if selected_mbti:
        st.markdown("<p style='text-align: center; font-size: 22px; color: #8A2BE2;'>✨ 하호님의 MBTI는 바로... <span style='color: #FF4500; font-weight: bold;'>{}</span> 이시군요! ✨</p>".format(selected_mbti), unsafe_allow_html=True)

        # ⏳ 결과 로딩 스피너 (짜잔! 하는 효과!)
        with st.spinner('🤔 하호님에게 딱 맞는 취미를 열심히 찾고 있어요... 잠시만 기다려주세요! 🌟'):
            time.sleep(2) # 2초 동안 기다리게 합니다. 실제로는 여기서 DB 조회 등을 할 수 있겠죠!

        st.markdown(f"<h3 style='text-align: center; color: #FF1493; font-size: 30px;'>🎉 {selected_mbti} 유형의 하호님을 위한 반짝이는 취미들이에요! ✨</h3>", unsafe_allow_html=True)

        # 선택된 MBTI 친구의 취미 리스트를 찾아와요!
        recommended_hobbies = mbti_hobbies[selected_mbti]

        # 찾아온 취미들을 예쁘게 리스트로 보여드려요! 💖 (컬럼을 사용해서 더 보기 좋게!)
        num_columns = 2 if len(recommended_hobbies) > 2 else 1 # 취미 개수에 따라 컬럼 조절
        cols = st.columns(num_columns) # 여러 개의 컬럼 생성

        for i, hobby_html in enumerate(recommended_hobbies):
            with cols[i % num_columns]: # 각 컬럼에 취미를 배분
                st.markdown(f"<p style='background-color: #F0F8FF; padding: 10px; border-radius: 10px; margin-bottom: 10px; border: 1px solid #E0FFFF; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);'>{hobby_html}</p>", unsafe_allow_html=True)
                # st.success(hobby_html, icon="🎁") # 또 다른 표시 방법

        st.markdown("---")
        st.markdown("<h3 style='text-align: center; color: #4682B4;'>어떠세요? 하호님 마음에 쏙 드는 취미가 있었으면 좋겠네요! 🥰</h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #CD5C5C;'>다른 MBTI 친구들의 취미도 궁금하다면 위에서 다시 선택해보세요! 뿅! ✨</h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #20B2AA;'>취미와 함께 행복하고 즐거운 시간 보내시길 하웅이가 응원할게요! ㅎㅎ 🥳</h3>", unsafe_allow_html=True)

        # 💌 하단에 작은 메시지
        st.markdown("<br><p style='text-align: center; font-size: 14px; color: #708090;'>created with 💖 by 하웅 (for 하호님) </p>", unsafe_allow_html=True)


# 이 파일이 혼자 실행될 때! 마법처럼 웹 앱이 나타나도록 준비하는 주문이에요! 🪄
if __name__ == "__main__":
    # st.set_page_config는 반드시 함수 호출 전에, 그리고 한 번만 있어야 합니다.
    # 여러 번 호출되거나 함수 내부에 있으면 에러가 발생할 수 있어요!
    st.set_page_config(
        page_title="💖 MBTI 취미 추천 타로 마법진 🔮",
        layout="centered", # wide 또는 centered 선택 가능
        initial_sidebar_state="expanded", # collapsed, expanded, auto 선택 가능
        page_icon="🎉" # 브라우저 탭에 표시될 아이콘
    )
    mbti_hobby_recommender_app_flashy()
