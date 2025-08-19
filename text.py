import streamlit as st
import pandas as pd
from datetime import datetime
import random
from PIL import Image
import requests
from io import BytesIO
import base64

# 페이지 기본 설정
st.set_page_config(
    page_title="계절별 국내 여행지 추천",
    page_icon="🏝️",
    layout="wide" # 전체 너비를 사용하도록 설정
)

# --- CSS 스타일링 (더욱 예쁘게 꾸미기) ---
st.markdown("""
<style>
    /* 전체 앱 배경 투명하게, 카드만 흰색 배경 */
    .stApp {
        background-color: rgba(0,0,0,0); /* 기본 배경은 투명으로 설정하여 배경 이미지 보이도록 */
    }
    
    /* 실제 내용이 들어가는 블록 컨테이너에만 배경색 적용 */
    .block-container {
        background-color: rgba(255, 255, 255, 0.9); /* 내용 영역에만 반투명 흰색 배경 */
        border-radius: 15px;
        padding: 3rem; /* 여백 더 넓게 */
        box-shadow: 0 8px 16px rgba(0,0,0,0.2); /* 그림자 강화 */
        margin-top: 2rem; /* 위쪽 여백 */
        margin-bottom: 2rem; /* 아래쪽 여백 */
    }

    /* 메인 타이틀 */
    .main-header {
        font-size: 2.8rem; /* 폰트 크기 키움 */
        color: #007BFF; /* 진한 파란색 */
        text-align: center;
        margin-bottom: 1.5rem;
        font-weight: 800; /* 더 굵게 */
        text-shadow: 3px 3px 6px rgba(0,0,0,0.2); /* 그림자 더 선명하게 */
    }
    
    /* 서브 타이틀 (추천 여행지) */
    .sub-header {
        font-size: 2.2rem; /* 폰트 크기 키움 */
        color: #28A745; /* 녹색 */
        margin-top: 3rem;
        margin-bottom: 1.5rem;
        text-align: center;
        font-weight: 700;
    }
    
    /* 카드 디자인 */
    .card {
        border-radius: 15px; /* 모서리 둥글게 */
        padding: 1.8rem; /* 패딩 키움 */
        margin-bottom: 2rem;
        background-color: #FFFFFF; /* 흰색 배경 */
        box-shadow: 0 6px 12px rgba(0,0,0,0.15); /* 그림자 */
        transition: transform 0.2s ease-in-out; /* 호버 효과 */
        border: 1px solid #e0e0e0; /* 테두리 추가 */
    }
    .card:hover {
        transform: translateY(-8px); /* 마우스 올리면 살짝 위로 */
    }

    /* 여행지 이름 */
    .destination-name {
        color: #0056b3; /* 진한 파란색 */
        font-weight: bold;
        font-size: 1.6rem; /* 폰트 크기 키움 */
        margin-bottom: 0.8rem;
    }

    /* 태그 스타일 */
    .tag {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 20px; /* 더 둥글게 */
        font-size: 0.9rem;
        font-weight: 600;
        margin-right: 8px;
        margin-bottom: 8px;
        white-space: nowrap; /* 줄바꿈 방지 */
    }

    .location-tag { background-color: #E0F7FA; color: #00796B; } /* 청록 계열 */
    .group-tag { background-color: #E8F5E9; color: #388E3C; } /* 녹색 계열 */
    .type-tag { background-color: #FFF3E0; color: #EF6C00; } /* 주황 계열 */

    /* 사이드바 헤더 */
    .sidebar-header {
        font-size: 1.5rem; /* 폰트 크기 키움 */
        font-weight: bold;
        color: #1A237E; /* 어두운 남색 */
        margin-bottom: 1rem;
        border-bottom: 2px solid #C5CAE9; /* 아래쪽 테두리 */
        padding-bottom: 0.5rem;
    }

    /* Streamlit 기본 텍스트 색상 조정 */
    .stMarkdown h3 {
        color: #4CAF50; /* 초록색 */
    }
    .stMarkdown strong {
        color: #D32F2F; /* 빨간색 강조 */
    }
    .stMarkdown p {
        font-size: 1.1rem;
        line-height: 1.6;
        color: #333;
    }
    
    /* Streamlit 버튼 스타일 */
    div.stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #45a049;
    }

</style>
""", unsafe_allow_html=True)

# 배경 이미지 설정 함수 (Unsplash에서 여행 관련 이미지 URL 사용)
def add_bg_from_url(url):
    try:
        response = requests.get(url, timeout=5) # 타임아웃 추가
        response.raise_for_status() # HTTP 에러 발생 시 예외 처리
        img = Image.open(BytesIO(response.content))
        img_bytes = BytesIO()
        img.save(img_bytes, format='PNG') # PNG 형식으로 저장 (JPEG도 가능하지만 투명도 문제 고려)
        encoded = base64.b64encode(img_bytes.getvalue()).decode()
        
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed; /* 스크롤해도 배경 고정 */
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except requests.exceptions.RequestException as e:
        st.error(f"배경 이미지를 불러오는 데 실패했습니다: {e}")
    except Exception as e:
        st.error(f"이미지 처리 중 오류 발생: {e}")

# 현재 계절 확인 함수
def get_current_season():
    now = datetime.now()
    month = now.month
    
    if 3 <= month <= 5:
        return "봄", "https://images.unsplash.com/photo-1549405076-788e0b04c868" # 벚꽃, 봄 배경
    elif 6 <= month <= 8:
        return "여름", "https://images.unsplash.com/photo-1582053245084-5a639b56360c" # 여름 바다 배경
    elif 9 <= month <= 11:
        return "가을", "https://images.unsplash.com/photo-1473225071151-cf4615a77038" # 단풍, 가을 배경
    else:
        return "겨울", "https://images.unsplash.com/photo-1490806450637-a9a7a9dc1972" # 눈 덮인 겨울 배경

# 여행지 데이터 (상세 정보 추가)
# 각 여행지에 "target_group" (누구와 함께?) 및 "travel_type" (어떤 종류의 여행?) 필드를 추가
travel_data = {
    "봄": [
        {
            "name": "제주 유채꽃 축제",
            "location": "제주도",
            "description": "노란 유채꽃이 온 들판을 가득 채워 환상적인 봄을 선사하는 곳입니다. 사진 찍기 좋고, 여유로운 산책을 즐기기 좋아요.",
            "image": "https://images.unsplash.com/photo-1592378596855-9e829f74d4b9",
            "target_group": ["가족", "친구", "연인", "개인"],
            "travel_type": ["자연", "축제", "힐링", "꽃놀이", "사진"]
        },
        {
            "name": "진해 군항제 (벚꽃 축제)",
            "location": "경상남도 창원시",
            "description": "국내 최대 규모의 벚꽃 축제로 군항제와 함께 열립니다. 밤 벚꽃도 아름다우며, 다양한 볼거리가 가득해요.",
            "image": "https://images.unsplash.com/photo-1522383225653-ed111181a951",
            "target_group": ["가족", "친구", "연인", "개인"],
            "travel_type": ["축제", "문화", "꽃놀이", "도시"]
        },
        {
            "name": "보성 녹차밭",
            "location": "전라남도 보성군",
            "description": "푸른 녹차밭과 봄의 신선한 공기를 느끼며 힐링할 수 있는 곳입니다. 녹차 아이스크림도 꼭 맛보세요!",
            "image": "https://images.unsplash.com/photo-1576089073624-b5059084a104",
            "target_group": ["친구", "연인", "개인"],
            "travel_type": ["자연", "힐링", "사진", "먹거리"]
        },
        {
            "name": "경주 보문단지",
            "location": "경상북도 경주시",
            "description": "벚꽃으로 유명한 관광단지로, 보문호반길을 따라 자전거를 타거나 유람선을 탈 수 있습니다.",
            "image": "https://images.unsplash.com/photo-1616421394747-0e628b030432",
            "target_group": ["가족", "친구", "연인", "개인"],
            "travel_type": ["역사", "자연", "힐링", "액티비티"]
        },
        {
            "name": "아침고요수목원",
            "location": "경기도 가평군",
            "description": "다양한 테마의 정원과 아름다운 꽃들이 가득한 곳으로, 계절마다 색다른 풍경을 자랑합니다.",
            "image": "https://images.unsplash.com/photo-1558230559-05d5c07b4d37",
            "target_group": ["가족", "친구", "연인", "개인"],
            "travel_type": ["자연", "힐링", "사진", "산책"]
        },
    ],
    "여름": [
        {
            "name": "속초 해수욕장",
            "location": "강원도 속초시",
            "description": "맑고 푸른 동해 바다에서 시원한 여름을 만끽할 수 있는 인기 해수욕장입니다. 서핑 등 해양 레저도 즐길 수 있어요.",
            "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
            "target_group": ["가족", "친구", "연인"],
            "travel_type": ["바닷가", "액티비티", "휴양", "물놀이"]
        },
        {
            "name": "남이섬",
            "location": "강원도 춘천시",
            "description": "울창한 메타세쿼이아 숲길과 시원한 강바람을 즐길 수 있는 섬입니다. 자전거 타기, 스카이라인 짚와이어 등 다양한 활동이 가능해요.",
            "image": "https://images.unsplash.com/photo-1588392382834-a891154bca4d",
            "target_group": ["가족", "친구", "연인"],
            "travel_type": ["자연", "힐링", "액티비티", "문화"]
        },
        {
            "name": "제주 서귀포 올레길",
            "location": "제주도 서귀포시",
            "description": "바다를 따라 걸으며 시원한 바다 풍경과 제주의 아름다운 자연을 감상할 수 있는 트레킹 코스입니다.",
            "image": "https://images.unsplash.com/photo-1501426026826-31c667bdf23d",
            "target_group": ["친구", "연인", "개인"],
            "travel_type": ["액티비티", "자연", "트레킹", "힐링"]
        },
        {
            "name": "대구 이월드 & 우방타워랜드",
            "location": "대구광역시",
            "description": "다양한 놀이기구와 워터파크 시설을 갖춘 도심형 테마파크입니다. 밤에는 조명도 아름다워요.",
            "image": "https://images.unsplash.com/photo-1569429593410-b498b3fb3387",
            "target_group": ["가족", "친구", "연인"],
            "travel_type": ["액티비티", "도시", "테마파크"]
        },
        {
            "name": "여수 밤바다 (돌산공원 & 해상케이블카)",
            "location": "전라남도 여수시",
            "description": "낭만적인 여수 밤바다의 풍경을 감상할 수 있는 명소입니다. 해상 케이블카를 타고 바다 위를 가로질러 보세요.",
            "image": "https://images.unsplash.com/photo-1631558237272-359f49b1a03f",
            "target_group": ["연인", "친구", "가족"],
            "travel_type": ["도시", "야경", "힐링", "사진"]
        },
    ],
    "가을": [
        {
            "name": "내장산 국립공원",
            "location": "전라북도 정읍시",
            "description": "화려한 단풍으로 유명한 국립공원입니다. 가을 산행과 단풍 구경을 제대로 즐길 수 있어요.",
            "image": "https://images.unsplash.com/photo-1509224863479-ab583ee78692",
            "target_group": ["가족", "친구", "연인", "개인"],
            "travel_type": ["산", "자연", "트레킹", "사진"]
        },
        {
            "name": "설악산 국립공원",
            "location": "강원도 속초시",
            "description": "가을 단풍이 절경을 이루는 명산입니다. 케이블카를 이용하면 쉽게 정상 부근까지 오를 수 있어요.",
            "image": "https://images.unsplash.com/photo-1508193638397-1c4234db14d8",
            "target_group": ["친구", "연인", "가족"],
            "travel_type": ["산", "액티비티", "자연", "트레킹"]
        },
        {
            "name": "안동 하회마을",
            "location": "경상북도 안동시",
            "description": "전통 한옥과 가을 풍경이 어우러진 유네스코 세계문화유산입니다. 전통 공연도 감상할 수 있어요.",
            "image": "https://images.unsplash.com/photo-1578167635644-637c6330eaea",
            "target_group": ["가족", "친구", "개인"],
            "travel_type": ["문화", "역사", "힐링", "사진"]
        },
        {
            "name": "순천만 습지",
            "location": "전라남도 순천시",
            "description": "황금빛 억새와 갈대가 장관을 이루는 생태공원입니다. 일몰 풍경이 특히 아름다워요.",
            "image": "https://images.unsplash.com/photo-1572203265299-d2372aaaa178",
            "target_group": ["가족", "친구", "연인", "개인"],
            "travel_type": ["자연", "힐링", "사진"]
        },
        {
            "name": "담양 죽녹원",
            "location": "전라남도 담양군",
            "description": "푸른 대나무 숲길을 걸으며 맑은 공기를 마실 수 있는 힐링 공간입니다. 가을에도 상쾌해요.",
            "image": "https://images.unsplash.com/photo-1558914619-74d470d04c3c",
            "target_group": ["가족", "친구", "연인", "개인"],
            "travel_type": ["자연", "힐링", "사진", "산책"]
        },
    ],
    "겨울": [
        {
            "name": "평창 스키리조트",
            "location": "강원도 평창군",
            "description": "국내 최고의 스키 리조트에서 눈 덮인 설원을 만끽하며 겨울 스포츠를 즐길 수 있습니다.",
            "image": "https://images.unsplash.com/photo-1551698618-1dfe5d97d256",
            "target_group": ["친구", "연인", "가족"],
            "travel_type": ["액티비티", "스포츠", "겨울", "스키/보드"]
        },
        {
            "name": "태백산 눈꽃축제",
            "location": "강원도 태백시",
            "description": "하얀 설원과 눈꽃이 아름다운 겨울 축제입니다. 웅장한 설경을 배경으로 멋진 추억을 남겨보세요.",
            "image": "https://images.unsplash.com/photo-1491002052546-bf38f186af56",
            "target_group": ["가족", "친구", "연인", "개인"],
            "travel_type": ["축제", "자연", "겨울", "사진"]
        },
        {
            "name": "인제 빙어축제",
            "location": "강원도 인제군",
            "description": "얼음낚시와 다양한 겨울 체험을 할 수 있는 축제입니다. 가족과 함께 특별한 겨울 추억을 만들어요.",
            "image": "https://images.unsplash.com/photo-1520262454473-a1a82276a574",
            "target_group": ["가족", "친구"],
            "travel_type": ["축제", "액티비티", "겨울", "체험"]
        },
        {
            "name": "서울 덕수궁 돌담길 (겨울)",
            "location": "서울특별시",
            "description": "눈 내린 고즈넉한 돌담길을 걸으며 겨울의 낭만을 느낄 수 있습니다. 근처 박물관도 함께 방문하기 좋아요.",
            "image": "https://images.unsplash.com/photo-1627918451871-3c72b212f45c",
            "target_group": ["연인", "친구", "개인"],
            "travel_type": ["도시", "문화", "힐링", "사진"]
        },
        {
            "name": "아침고요수목원 오색별빛정원전",
            "location": "경기도 가평군",
            "description": "겨울밤을 아름다운 빛으로 수놓는 환상적인 조명 축제입니다. 연인 또는 가족과 함께 로맨틱한 분위기를 만끽하세요.",
            "image": "https://images.unsplash.com/photo-1542845942-8354c0b48f9e", # 야경 조명 축제 이미지
            "target_group": ["가족", "연인", "친구", "개인"],
            "travel_type": ["축제", "힐링", "사진", "야경"]
        }
    ]
}

# --- 메인 함수 ---
def main():
    # 현재 계절 및 배경 이미지 URL 가져오기
    current_season, bg_image_url = get_current_season()
    add_bg_from_url(bg_image_url) # 현재 계절에 맞는 배경 이미지 설정

    # 메인 제목
    st.markdown(f'<div class="main-header">✨ {current_season}의 <span style="color:#FFD700;">국내 여행지</span> 추천 ✨</div>', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #666;'>여행 가는 듯 설레는 마음으로 나만의 맞춤 여행지를 찾아보세요! 💖</h3>", unsafe_allow_html=True)

    st.markdown("---")

    # --- 사이드바 필터 ---
    st.sidebar.markdown('<div class="sidebar-header">나만의 여행 찾기 🚀</div>', unsafe_allow_html=True)

    # 1. 누구와 함께 가시나요? (선택 상자)
    who_options = ["누구와든 좋아요! (전체 보기)", "가족", "친구", "연인", "개인"]
    who_with = st.sidebar.selectbox(
        "🙋‍♀️ **누구와 함께 가시나요?**",
        who_options,
        index=0 # 기본값: "누구와든 좋아요! (전체 보기)"
    )

    # 2. 어떤 종류의 여행을 원하시나요? (다중 선택 상자)
    # 여행 유형 옵션을 동적으로 관리하거나, 필요한 경우 미리 정의
    all_travel_types = sorted(list(set([t for season in travel_data.values() for item in season for t in item["travel_type"]])))
    
    travel_preferences = st.sidebar.multiselect(
        "🗺️ **어떤 종류의 여행을 원하시나요? (다중 선택 가능)**",
        all_travel_types,
        default=[] # 기본값: 아무것도 선택되지 않음
    )

    # 필터 초기화 버튼
    if st.sidebar.button("필터 초기화"):
        st.experimental_rerun() # 앱을 다시 실행하여 필터 초기화 효과

    st.sidebar.markdown("---")
    st.sidebar.info("선택 필터가 많아질수록 더욱 **정확한 추천**을 받을 수 있어요! 😉")

    # --- 여행지 필터링 로직 ---
    season_destinations = travel_data.get(current_season, [])
    
    filtered_destinations = []
    for dest in season_destinations:
        # 1. '누구와' 필터 적용
        # "누구와든 좋아요!" 선택 시에는 이 필터를 건너김
        if who_with != "누구와든 좋아요! (전체 보기)":
            if who_with not in dest.get("target_group", []):
                continue # 현재 여행지가 선택된 대상 그룹에 속하지 않으면 다음 여행지로

        # 2. '어떤 종류의' 필터 적용
        # 사용자가 아무것도 선택하지 않았다면 이 필터를 건너김
        if travel_preferences:
            # 선택된 모든 여행 취향이 여행지의 travel_type에 포함되어야 함 (AND 조건)
            # any()를 사용하여 '하나라도' 일치하면 필터링되도록 할 수도 있습니다.
            # 여기서는 '모두 포함되어야' 더 정밀한 추천이 되도록 all() 사용
            if not all(pref in dest.get("travel_type", []) for pref in travel_preferences):
                continue

        filtered_destinations.append(dest)

    # --- 필터링된 여행지 표시 ---
    if filtered_destinations:
        st.markdown(f'<div class="sub-header">🎉 하호님을 위한 {current_season} 추천 여행지 🎉</div>', unsafe_allow_html=True)
        
        # 여행지가 짝수든 홀수든 깔끔하게 2열로 정렬
        cols = st.columns(2) 
        
        for i, destination in enumerate(filtered_destinations):
            with cols[i % 2]: # i % 2를 이용해 0번째 열, 1번째 열을 번갈아 가며 사용
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.image(destination["image"], caption=f"{destination['name']} - {destination['location']}", use_column_width=True)
                st.markdown(f'<div class="destination-name">{destination["name"]}</div>', unsafe_allow_html=True)
                st.markdown(f'**<span class="location-tag">📍 {destination["location"]}</span>**', unsafe_allow_html=True)
                st.markdown(f"") # 한 칸 띄우기
                st.markdown(f"💖 **추천 포인트:** {destination['description']}")
                
                # '누구와' 태그 표시
                st.markdown(f'**👨‍👩‍👧‍👦 추천 대상:** {" ".join([f"<span class='tag group-tag'>{group}</span>" for group in destination.get("target_group", [])])}', unsafe_allow_html=True)
                
                # '여행 테마' 태그 표시
                st.markdown(f'**🌈 여행 테마:** {" ".join([f"<span class='tag type-tag'>{_type}</span>" for _type in destination.get("travel_type", [])])}', unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True) # 카드 닫기
    else:
        st.info(f"😢 아쉽게도 선택하신 조건에 맞는 **{current_season} 여행지**는 찾을 수 없었어요. 다른 조건을 선택해보시거나, **'누구와든 좋아요!'** 옵션으로 넓게 찾아보시는 건 어떠세요?")

    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #999;'>즐거운 여행 계획에 하웅이의 추천이 도움이 되었기를 바라요! ✈️</p>", unsafe_allow_html=True)


# Streamlit 앱 실행
if __name__ == "__main__":
    main()

