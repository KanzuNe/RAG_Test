from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings

loader = TextLoader(r"D:\CODING\RAG Test\quy_che.txt", encoding="utf-8")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=20)
docs = text_splitter.split_documents(documents)

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

db = Chroma.from_documents(docs, embedding_function)

res = db.similarity_search(query="Điểm tổng kết tính thế nào", k=2)

print(res)