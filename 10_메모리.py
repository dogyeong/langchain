from langchain_openai import ChatOpenAI
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

store = {}  # 세션 기록을 저장할 딕셔너리

# 세션 ID를 기반으로 세션 기록을 가져오는 함수
def get_session_history(session_ids: str) -> BaseChatMessageHistory:
    print(session_ids)
    if session_ids not in store:  # 세션 ID가 store에 없는 경우
        # 새로운 ChatMessageHistory 객체를 생성하여 store에 저장
        store[session_ids] = ChatMessageHistory()
    return store[session_ids]  # 해당 세션 ID에 대한 세션 기록 반환

############################################################################################################

llm = ChatOpenAI(model_name='gpt-4o')
prompt = ChatPromptTemplate.from_messages([
  ("human", "진희는 강아지를 한마리 키우고 있습니다."),
  ("human", "영수는 고양이를 두마리 키우고 있습니다."),
  ("human", "{input}"),
])

chain = prompt | llm

chain_with_history = RunnableWithMessageHistory(chain, get_session_history=get_session_history)
 
print(
    chain_with_history.invoke(
        { "input": "진희와 영수가 키우는 동물은 총 몇마리?" },
        config={"configurable": {"session_id": "abc123"}},
    )
    .content
)




