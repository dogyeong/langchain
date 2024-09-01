from langchain_huggingface import HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="microsoft/Phi-3-mini-4k-instruct",  # 모델 저장소 ID를 지정합니다.
    max_new_tokens=256,  # 생성할 최대 토큰 길이를 설정합니다.
    temperature=0.1,
    huggingfacehub="",  # 허깅페이스 토큰
)

response = llm.invoke("진희는 강아지를 키우고 있습니다. 진희가 키우고 있는 동물은?")
print(response)
