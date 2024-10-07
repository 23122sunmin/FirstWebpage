import streamlit as st
import random
import datetime

st.title(':sparkles:로또 자동 생성기:sparkles:')

# 로또 번호 추첨 함수 (1 ~ 3까지 번호 생성)
def generate_lotto(length=10):
    return [random.randint(1, 3) for _ in range(length)]  # 지정된 길이만큼 번호를 생성

# 자동 생성 후 추첨 버튼
if st.button('자동 생성 후 추첨'):
    drawn_numbers = generate_lotto()  # 10개의 숫자를 자동으로 생성
    hidden_lotto = generate_lotto()  # 숨겨진 정답 번호도 10개 생성

    # 추첨된 번호를 초록색으로 크게 표시
    st.markdown(f"### 추첨된 번호: <span style='color: green; font-size: 36px;'>{drawn_numbers}</span>", unsafe_allow_html=True)
    
    # 맞춘 번호 계산
    matched_numbers = set(drawn_numbers).intersection(hidden_lotto)
    match_count = len(matched_numbers)

    # 결과 표시 (맞춘 숫자 삭제)
    st.write(f'총 맞춘 개수: {match_count}')

    # 시각 표시
    st.write(f"추첨된 시각: {datetime.datetime.now().strftime('%y-%m-%d %H:%M')}")
