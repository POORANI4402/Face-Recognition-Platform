import os
os.environ["OPENAI_API_KEY"] = "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"
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not set in environment variables")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def setup_rag(txt_file_path):
    loader = TextLoader(file_path=txt_file_path, encoding="utf-8")
    raw_docs = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(raw_docs)

    if len(docs) == 0:
        raise ValueError("No documents found to process. Check your text file.")

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embedding=embeddings)

    llm = ChatOpenAI(temperature=0.7, model_name="gpt-4")
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

    return chain
