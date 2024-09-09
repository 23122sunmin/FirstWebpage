import streamlit as st
st.title("my first web servixe!!")
name=st.text_input("이름을 입력해주세요!")
menu=st.selectbox("좋아하는 음식을 선택해주세요!",['셱셱','베라','그릭요거트','파스타'])
if st.button("제출"):
    st.write(name+"님! 당신이 좋아하는 음식은 "+menu+"이군요! 저도 좋아요!")
