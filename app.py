import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from sheets import save_to_sheet

st.set_page_config(page_title="AI English Tutor", page_icon="📘")
st.title("📘 AI English Tutor")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=st.secrets["GROQ_API_KEY"]
)

question = st.text_input("Ask your English question")

if st.button("Ask"):
    if question.strip():
        response = llm.invoke([HumanMessage(content=question)])
        answer = response.content
        save_to_sheet(question, answer)
        st.success("Answer generated!")
        st.write(answer)
    else:
        st.warning("Please enter a question.")