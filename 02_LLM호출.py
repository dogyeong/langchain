from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name='gpt-4o')

print(llm.invoke("진희는 강아지를 키우고 있습니다. 진희가 키우고 있는 동물은?").content)