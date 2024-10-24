import marqo
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Marqo
from langchain_text_splitters import CharacterTextSplitter


loader = TextLoader("test.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

mq = marqo.Client(url='http://192.168.1.3:8882')

index_name = "my-first-index"

# incase the demo is re-run
try:
    mq.delete_index(index_name)
except Exception:
    print(f"Creating {index_name}")

mq.create_index(index_name)

# Insert documents into Marqo index
for i, doc in enumerate(docs):
    document = {
        "_id": f"doc_{i}",
        "text": doc.page_content,  # Access the text content attribute
        # Add any other metadata here if necessary
    }
    mq.index(index_name).add_documents([document], tensor_fields=["text"])

# results = mq.index(index_name).search(
#     q="What did the president say about Ketanji Brown Jackson?", similarity_search_with_score=True)

# print(results)
