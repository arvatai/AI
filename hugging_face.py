from langchain_community.document_loaders import TextLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_postgres.vectorstores import PGVector


def load_and_split_documents(file_path, chunk_size=500, chunk_overlap=0):
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load() 
    
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs

def add_documents_to_db( connection, collection_name, file_path):

    docs = load_and_split_documents(file_path)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    db = PGVector.from_documents(embedding=embeddings, documents=docs,collection_name=collection_name, connection=connection,pre_delete_collection=True)
    print(f"Documents added to collection '{collection_name}' in the database.")

# Usage
if __name__ == "__main__":

    connection = "postgresql+psycopg://postgres:lovedeep@192.168.1.3:5432/vector_db"
    collection_name = "state_of_the_union_vectors"
    file_path = "test.txt"
    
    add_documents_to_db( connection, collection_name, file_path)
