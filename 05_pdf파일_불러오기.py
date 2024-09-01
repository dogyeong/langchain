from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("./The_Adventures_of_Tom_Sawyer.pdf")
document = loader.load()

print(document[5].page_content[:5000])