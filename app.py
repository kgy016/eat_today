import streamlit as st
import random
import time

# 1. 페이지 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍴")

# 2. 스타일링 (병맛 감성 한 스푼)
st.title("🍚 결정장애 구원자: 오늘 뭐 먹지?")
st.write("메뉴 고르기 힘드시죠? 그냥 기계의 선택에 운명을 맡기세요.")

# 3. 메뉴 데이터 관리
# 기본 메뉴 리스트
default_menu = [
    "김치찌개", "된장찌개", "제육덮밥", "비빔밥", "국밥", "칼국수", 
    "짜장면", "짬뽕", "탕수육", "마라탕", "쌀국수",
    "돈까스", "초밥", "라멘", "규동",
    "파스타", "피자", "스테이크", "샌드위치",
    "햄버거", "치킨", "떡볶이", "편의점 도시락"
]

# 사이드바에서 방문자가 메뉴를 수정할 수 있게 합니다.
with st.sidebar:
    st.header("⚙️ 메뉴 리스트 설정")
    st.write("싫어하는 메뉴는 지우고, 좋아하는 메뉴를 추가해 보세요!")
    menu_input = st.text_area("메뉴 목록 (쉼표로 구분)", value=", ".join(default_menu), height=300)
    menus = [m.strip() for m in menu_input.split(",") if m.strip()]

# 4. 메인 기능 실행
st.divider()

if st.button("🔥 운명의 메뉴 뽑기", use_container_width=True):
    if not menus:
        st.error("메뉴 리스트가 비어있어요! 사이드바에서 메뉴를 추가해 주세요.")
    else:
        # 긴장감 조성을 위한 로딩 효과
        progress_text = "오늘의 운명을 계산하는 중..."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        
        # 랜덤 선택
        selected = random.choice(menus)
        
        # 결과 발표
        st.balloons() # 풍선 효과
        st.markdown(f"<h1 style='text-align: center; color: #FF4B4B;'>🎊 {selected} 🎊</h1>", unsafe_content=True)
        st.markdown("<p style='text-align: center; font-size: 20px;'>오늘 당신의 운명은 이것입니다!</p>", unsafe_content=True)
        
        # 하찮은 코멘트 랜덤 출력
        comments = [
            "역시 이게 당겼죠? 고민 말고 고!",
            "마음에 안 들어도 어쩔 수 없어요. 기계의 선택은 냉정합니다.",
            "오늘 이거 안 먹으면 밤에 침대에서 생각날걸요?",
            "탁월한 선택입니다. 역시 당신의 운명!",
            "혹시... 다시 뽑으려고 버튼에 마우스 올린 거 아니죠? 다 압니다.",
            "다이어트는 내일부터! 일단 맛있게 드세요."
        ]
        st.success(random.choice(comments))

# 5. 푸터
st.divider()
st.caption("주의: 결과에 불만이 있어도 개발자는 책임지지 않습니다. 마음에 안 들면 '될 때까지' 누르는 게 국룰입니다.")
