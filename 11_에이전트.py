from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import create_tool_calling_agent, AgentExecutor

llm = ChatOpenAI(model_name='gpt-3.5-turbo')

prompt = ChatPromptTemplate.from_messages([
  ("human", "{input}"),
  MessagesPlaceholder(variable_name="agent_scratchpad")
])

tools = load_tools(["wikipedia", "llm-math"], llm=llm) #llm-math의 경우 나이 계산을 위해 사용

agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_executor.invoke({ "input": "애드 시런의 2024년 나이는?" })