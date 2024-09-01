from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(model_name='gpt-4o')
prompt = PromptTemplate.from_template("{country}의 수도는 어디야?")

chain = prompt | llm

print(chain.invoke("대한민국").content)