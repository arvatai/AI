import marqo
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Marqo
from langchain_text_splitters import CharacterTextSplitter

mq = marqo.Client(url='http://localhost:8882')

index_name = "my-first-index"

# Search query
query = "Can you help with the following scenario. We have a campaign on a daily budget of £10.  At 12pm we would put this budget to 2x so effectively this would now be £20 giving it an extra £10.  However if we manually change this budget to another value (say £30), what will happen to the base budget.  As we have changed the budget when its on 2x, will this affect the base budget. i.e will the abse budget be now £15, or will £30 be the base budget (in which case when it goes to 2x the following day the £30 would then go to £60) etc.  Ideally we would need the base budget to be reflected in this change to the £15."

# Perform the search
results = mq.index(index_name).search(q=query)

# Print the lenght of the search results
print(f"Number of search results: {len(results['hits'])}")

# Print search results with scores
for hit in results['hits']:
    print(f"Document ID: {hit['_id']}, Score: {hit['_score']}, Text: {hit['text']}")