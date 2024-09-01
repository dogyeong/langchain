from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(model_name='gpt-4o')

output_parser = CommaSeparatedListOutputParser()
format_instructions = output_parser.get_format_instructions()

prompt = PromptTemplate.from_template("7개의 팀을 보여줘 {subject}.\n{format_instructions}")

output=llm.invoke(prompt.format(subject="프로야구 팀", format_instructions=format_instructions)).content

print(output_parser.parse(output))