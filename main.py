import streamlit as st

# MBTI 데이터 정의
mbti_data = {
    "ENFP": {
        "직업": "크리에이티브 디렉터, 디자이너, 시나리오 작가, 방송 프로듀서",
        "잘 맞는 사람": "INFJ, INTJ (열정과 계획을 보완해주는 관계)"
    },
    "INFJ": {
        "직업": "직업상담사, 특수교사, 노인복지사, 아트 디렉터",
        "잘 맞는 사람": "ENFP, ENTP (공감과 직관이 조화를 이루는 관계)"
    },
    "INTJ": {
        "직업": "분석가, 경영 컨설턴트, 제약회사 연구원, 웹 개발자",
        "잘 맞는 사람": "ENTP, ENFP (아이디어와 실행력의 조화)"
    },
    "ESFP": {
        "직업": "코미디언, 의상 디자이너, 여행 상품 기획자",
        "잘 맞는 사람": "ISFJ, ISTJ (안정감을 주고받는 관계)"
    },
    # 필요에 따라 다른 MBTI 유형 추가
}

# Streamlit 앱 구성
st.title("MBTI 기반 직업 및 궁합 추천")

# 드롭다운 메뉴로 MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_data.keys()))

# 선택한 MBTI에 대한 정보 출력
if selected_mbti:
    st.subheader(f"선택한 MBTI: {selected_mbti}")
    st.write(f"**추천 직업:** {mbti_data[selected_mbti]['직업']}")
    st.write(f"**잘 맞는 사람:** {mbti_data[selected_mbti]['잘 맞는 사람']}")
