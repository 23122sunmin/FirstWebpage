import streamlit as st
import random
import datetime

st.title(':sparkles:로또 자동 생성기:sparkles:')

# 로또 번호 추첨 함수 (1 ~ 3까지 번호 생성)
def generate_lotto():
    lotto = set()
    while len(lotto) < 3:  # 1~3까지 3개를 생성
        number = random.randint(1, 3)
        lotto.add(number)
    return sorted(lotto)

# 숨겨진 정답 번호 생성
hidden_lotto = generate_lotto()

# 10회 자동 추첨 및 결과 비교
if st.button('자동 생성 후 추첨'):
    st.write(f'숨겨진 정답 번호: {hidden_lotto}')  # 실제로는 사용자에게 숨겨야 하지만 여기서는 확인을 위해 출력
    match_counts = []

    for i in range(10):
        user_lotto = generate_lotto()  # 자동 생성된 로또 번호
        matched_numbers = set(user_lotto).intersection(hidden_lotto)  # 일치하는 번호 계산
        match_counts.append(len(matched_numbers))

        st.write(f'[{i + 1}] 추첨된 번호: {user_lotto} | 맞춘 개수: {len(matched_numbers)}')

    # 총 맞춘 개수 표시
    total_matches = sum(match_counts)
    st.write(f'총 맞춘 개수: {total_matches}')

    # 시각 표시
    st.write(f"추첨된 시각: {datetime.datetime.now().strftime('%y-%m-%d %H:%M')}")
