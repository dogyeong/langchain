import streamlit as st
from langchain_openai import ChatOpenAI

st.set_page_config(page_title="🦜🔗 뭐든지 질문하세요~ ")
st.title('🦜🔗 뭐든지 질문하세요~ ')

with st.form('Question'):
    text = st.text_area('질문 입력:', 'What types of text models does OpenAI provide?') #첫 페이지가 실행될 때 보여줄 질문
    submitted = st.form_submit_button('보내기')
    
    # llm이 답변 생성
    llm = ChatOpenAI(model_name='gpt-4o')
    st.info(llm.invoke(text).content)
