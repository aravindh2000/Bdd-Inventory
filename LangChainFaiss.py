
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import faiss
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from docx.api import Document
text_splitter = CharacterTextSplitter(chunk_size=200,chunk_overlap=0)
document = Document("automate the process")
document.add_paragraph("automate the process")

docs = text_splitter.split_documents(documents=[document])
embd = OpenAIEmbeddings()
db = faiss.FAISS.from_documents(docs,embd)
print(db.index)