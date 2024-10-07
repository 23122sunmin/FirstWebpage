import streamlit as st
import random
import datetime

st.title(':sparkles:로또 생성기!!!!!!!!!!!!!!!!!!!!!:sparkles:')

# 보이지 않는(정답) 로또 번호 생성
def generate_hidden_lotto():
    hidden_lotto = set()
    while len(hidden_lotto) < 6:
        number = random.randint(1, 45)  # 일반적으로 로또 번호는 1~45
        hidden_lotto.add(number)
    hidden_lotto = list(hidden_lotto)
    hidden_lotto.sort()
    return hidden_lotto

# 일반 로또 번호 생성
def generate_lotto():
    lotto = set()
    while len(lotto) < 6:
        number = random.randint(1, 45)
        lotto.add(number)
    lotto = list(lotto)
    lotto.sort()
    return lotto

# 정답 로또 번호 생성 (보이지 않음)
hidden_lotto = generate_hidden_lotto()

button = st.button('로또 생성')

if button:
    st.subheader("정답 로또 번호 (숨김 처리)")
    st.write(hidden_lotto)  # Debugging purposes, this line can be hidden if you don't want to reveal the numbers.

    for i in range(1, 6):
        user_lotto = generate_lotto()
        highlighted_lotto = []

        # 자리와 숫자가 모두 일치할 때 노란색으로 표시 (HTML을 사용)
        for j in range(6):
            if user_lotto[j] == hidden_lotto[j]:
                highlighted_lotto.append(f'<span style="color:yellow">{user_lotto[j]}</span>')  # 노란색으로 표시
            else:
                highlighted_lotto.append(str(user_lotto[j]))

        # 로또 번호 출력 (HTML 스타일링 허용)
        st.markdown(f'{i}. 행운의 번호: {" ".join(highlighted_lotto)}', unsafe_allow_html=True)
    
    st.write(f"생성된 시각: {datetime.datetime.now().strftime("%y-%m-%d %H:%M")}')
