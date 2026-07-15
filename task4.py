from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_community.document_loaders import TextLoader
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("GEMINI_API_KEY")

loader = TextLoader(r"D:\CODING\RAG Test\quy_che.txt", encoding="utf-8")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=20)
docs = text_splitter.split_documents(documents)

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

db = Chroma.from_documents(docs, embedding_function)


os.environ["GOOGLE_API_KEY"] = key
llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")
ai_msg = llm.invoke("hello")
chat_template = ChatPromptTemplate.from_messages([
    ("Bạn là một trợ lí ảo của PTIT, hãy trả lời câu hỏi dựa vào context sau đây:{context}, câu hỏi là{input}")
])
document_chain = create_stuff_documents_chain(llm=llm,prompt=chat_template)
retrieve = db.as_retriever()
retrivial_chain = create_retrieval_chain(retrieve,document_chain)
response = retrivial_chain.invoke({"input": "Tôi không muốn bị đuổi khỏi phòng thi thì sao?"})
print(response)