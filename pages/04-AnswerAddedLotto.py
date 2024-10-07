import streamlit as st
import random
import datetime
import math

st.title(':sparkles:로또 번호 맞추기 게임:sparkles:')

# 로또 당첨 확률 계산 (1 ~ 9에서 6개를 선택하는 경우)
def calculate_lotto_probability():
    total_combinations = math.comb(9, 6)  # 9개 중 6개를 선택하는 조합
    return 1 / total_combinations

# 로또 번호 추첨 함수 (1 ~ 9까지 번호 생성)
def generate_lotto():
    lotto = set()
    while len(lotto) < 6:
        number = random.randint(1, 9)  # 1~9 사이의 숫자를 랜덤으로 선택
        lotto.add(number)
    lotto = list(lotto)
    lotto.sort()
    return lotto

# 당첨 확률 계산
probability = calculate_lotto_probability()

# 당첨 확률 표시
st.write(f"당첨될 확률: {probability:.10f}")

# 사용자 이름 입력
user_name = st.text_input('당신의 이름을 입력하세요:')

# 사용자가 선택한 번호를 받는 부분 (1~9 선택)
user_numbers = st.multiselect('번호를 선택하세요 (1~9)', list(range(1, 10)), default=[])

# 자동 생성 번호 저장 변수
auto_generated = False

# "자동 생성" 버튼을 눌렀을 때
if st.button('자동 생성'):
    user_numbers = generate_lotto()
    auto_generated = True
    st.write(f'자동 생성된 번호: {user_numbers}')

# 로또 번호 생성 및 결과 비교
if st.button('로또 번호 추첨'):
    if not user_name:
        st.error('이름을 입력해주세요!')
    elif not auto_generated and len(user_numbers) != 6:
        st.error('6개의 번호를 선택하거나 자동 생성 버튼을 눌러주세요!')
    else:
        if not auto_generated:
            user_numbers.sort()
            st.write(f'{user_name}님이 선택한 번호: {user_numbers}')
        
        lotto_numbers = generate_lotto()
        st.write(f'추첨된 로또 번호: {lotto_numbers}')
        
        # 맞춘 번호 계산
        matched_numbers = set(user_numbers).intersection(lotto_numbers)
        st.write(f'맞춘 번호: {list(matched_numbers)}')
        st.write(f'총 맞춘 개수: {len(matched_numbers)}')

        # 시각 표시
        st.write(f"추첨된 시각: {datetime.datetime.now().strftime('%y-%m-%d %H:%M')}")
