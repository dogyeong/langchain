from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("{product}를 홍보하기 위한 좋은 문구를 추천해줘.")

print(prompt.format(product="페인트"))