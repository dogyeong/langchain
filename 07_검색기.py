from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA

llm = ChatOpenAI(model_name='gpt-4o')

loader = PyPDFLoader("./The_Adventures_of_Tom_Sawyer.pdf")
document = loader.load()

embeddings = OpenAIEmbeddings()

db = FAISS.from_documents(document, embeddings)
retriever = db.as_retriever()

qa = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=retriever
  )

query = "마을 무덤에 있던 남자를 죽인 사람은 누구니?"
result = qa({ "query": query })
print(result['result'])