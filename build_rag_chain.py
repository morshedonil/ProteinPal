import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_huggingface import HuggingFaceEmbeddings
from vectorize import get_embedding_model
from langchain_chroma import Chroma
from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain

load_dotenv()

HF_TOKEN = os.environ.get("HF_TOKEN")
hugging_face_repo_id = "mistralai/Mistral-7B-Instruct-v0.3"

def load_huggingface_model():
    
    llm = HuggingFaceEndpoint(
       repo_id=hugging_face_repo_id,
       temperature = 0.5,
       max_new_tokens=512      
    )
       
    return llm

llm = load_huggingface_model()

def setup_prompt():

    custom_prompt_template = """
    You are a helpful assistant that can answer questions about food nutrition.
    You have access to a database of food items and their nutritional information.
    When asked a question, you will first search the database for relevant information,
    and then provide a concise answer based on the retrieved data.
    Here is the question: {question}
    context: {context}
    """

    prompt = PromptTemplate(
        input_variables=["question", "context"],
        template=custom_prompt_template
    )
    return prompt

embedding_model = get_embedding_model()
db = Chroma(persist_directory="vectorstore/chroma_db",
           embedding_function=embedding_model)

retriever = db.as_retriever()

contextualize_q_prompt = ChatPromptTemplate.from_messages([
("system", "Given a chat history and the latest user question "
               "which might reference context in the chat history, "
               "formulate a standalone question. Do NOT answer."),
MessagesPlaceholder("chat_history"),
("human", "{input}")
])

history_aware_retriever = create_history_aware_retriever(
    llm=llm,
    retriever=retriever,
    prompt=contextualize_q_prompt
    )

qa_chain = create_stuff_documents_chain(
    llm=llm,
    prompt=setup_prompt()
)

rag_chain = create_retrieval_chain(
    retriever=history_aware_retriever,
    combine_docs_chain=qa_chain
)

#### TESTING #####
# Optional: start with an empty chat history
chat_history = []

# Actual user query
question = input("Write your question here: ")

response = rag_chain.invoke({
    "input": question,           # For the history-aware retriever
    "chat_history": chat_history,  # Also for the retriever
    "question": question          # For the QA combine_docs_chain prompt
})

print("Answer:", response["answer"])
