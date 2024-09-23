import streamlit as st

st.title('2-7')

st.title('쌈@뽕한 첫 사이트 :sunglasses:')

st.header('이거 오ㅓㅏㄴ전 럭키비키잖아? :sparkles::sunglasses::sparkles:')

st.subheader(':thinking:')

st.caption('캡션은 짧은 설명을 추가하는 것!')

sample_code = '''
def function():
  print('겁내 쩔는 좌우명')
'''

st.code(sample_code, language="python")

st.text('내 좌우명을 입력해보았슴')

st.markdown('streamlit은 **마크다운 문법을 지원**합니다.')

st.markdown('텍스트의 색상을 :green[초록색]으로, **:blue[파란색 볼드체]**로 표현할 수도 있슴')

st.markdown(':green[$\sqrt{x^2+y^2}=1')

st.latex(r'\sqrt{x^2+y^2}=1')
