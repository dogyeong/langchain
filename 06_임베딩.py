import os
import asyncio
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

async def main():
  text = "진희는 강아지를 키우고 있습니다. 진희가 키우고 있는 동물은?"
  text_embedding = await embeddings.aembed_query(text)
  print(text_embedding)

asyncio.run(main())