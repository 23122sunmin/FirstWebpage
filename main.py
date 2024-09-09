import streamlit as st
st.title("음식 선호도 조사")
name=st.text_input("이름을 입력해주세요!")
menu=st.selectbox("좋아하는 음식을 선택해주세요!",['맥도날드','롯데리아','버거킹','kfc','맘스터치'])
if st.button("제출"):
    st.write(name+"님! 당신이 좋아하는 음식은 "+menu+"이군요! 저도 좋아요!")
