import marqo
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Marqo
from langchain_text_splitters import CharacterTextSplitter

mq = marqo.Client(url='http://192.168.1.3:8882')

index_name = "my-first-index"

results = mq.index(index_name).get_stats()

print(results)