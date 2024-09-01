import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(model_name='gpt-4o')
prompt = PromptTemplate.from_template("다음 문장을 한글로 번역해줘.\n\n{sentence}")
prompt2 = PromptTemplate.from_template("다음 문장을 한 문장으로 요약해줘.\n\n{sentence}")

chain = prompt | prompt2 | llm

sentence="""
One limitation of LLMs is their lack of contextual information (e.g., access to some specific documents or emails). You can combat this by giving LLMs access to the specific external data.
For this, you first need to load the external data with a document loader. LangChain provides a variety of loaders for different types of documents ranging from PDFs and emails to websites and YouTube videos.
"""

print(chain.invoke(sentence).content)