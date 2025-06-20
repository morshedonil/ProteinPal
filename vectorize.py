from get_data import get_raw_data, fetch_all_data, get_macro_data
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from sentence_transformers import SentenceTransformer
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma



def create_chunks(data):

    # Join the cleaned data into one string
    combined_text = '\n'.join(cleaned_data)

    # Wrap into a Document object
    docs = [Document(page_content=combined_text)] 

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    chunks = text_splitter.split_documents(docs)
    return chunks

raw_data = fetch_all_data()
cleaned_data = get_macro_data(raw_data)
text_chunks = create_chunks(cleaned_data)

def get_embedding_model():
    model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return model

model = get_embedding_model()

DB_PATH = "vectorstore/chroma_db"

db = Chroma.from_documents(text_chunks, embedding=model, persist_directory=DB_PATH)