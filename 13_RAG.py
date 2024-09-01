from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

documents = TextLoader("./AI.txt", "utf-8").load()

# 문서를 청크로 분할
def split_docs(documents,chunk_size=1000,chunk_overlap=20):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs

# docs 변수에 분할 문서를 저장
docs = split_docs(documents)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Chromdb에 벡터 저장
db = Chroma.from_documents(docs, embeddings)
llm = ChatOpenAI(model_name="gpt-4o")

# Q&A 체인을 사용하여 쿼리에 대한 답변 얻기
chain = load_qa_chain(llm, chain_type="stuff",verbose=True)

# 쿼리를 작성하고 유사성 검색을 수행하여 답변을 생성,따라서 txt에 있는 내용을 질의해야 합니다
query = "AI란?"
matching_docs = db.similarity_search(query)
answer =  chain.run(input_documents=matching_docs, question=query)
print(answer)




