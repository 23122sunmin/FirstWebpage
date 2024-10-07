import streamlit as st
import random
import datetime

st.title(':sparkles:로또 자동 생성기:sparkles:')

# 로또 번호 추첨 함수 (1 ~ 3까지 번호 생성)
def generate_lotto():
    lotto = []
    for _ in range(10):  # 10번 숫자를 생성
        number = random.randint(1, 3)
        lotto.append(number)
    return lotto

# 숨겨진 정답 번호 생성
hidden_lotto = [1, 2, 3]  # 예시로 숨길 정답 번호 설정

# 자동 생성 후 추첨 버튼
if st.button('자동 생성 후 추첨'):
    drawn_numbers = generate_lotto()  # 10개의 숫자를 자동으로 생성
    st.write(f'숨겨진 정답 번호: {hidden_lotto}')  # 실제로는 사용자에게 숨겨야 하지만 여기서는 확인을 위해 출력
    st.write(f'추첨된 번호: {drawn_numbers}')
    
    # 맞춘 번호 계산
    matched_numbers = set(drawn_numbers).intersection(hidden_lotto)
    match_count = len(matched_numbers)

    # 결과 표시
    st.write(f'맞춘 번호: {list(matched_numbers)}')
    st.write(f'총 맞춘 개수: {match_count}')
    
    # 시각 표시
    st.write(f"추첨된 시각: {datetime.datetime.now().strftime('%y-%m-%d %H:%M')}")
