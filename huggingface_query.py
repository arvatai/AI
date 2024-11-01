from langchain_huggingface import HuggingFaceEmbeddings
from langchain_postgres.vectorstores import PGVector

def similarity_search(connection, collection_name, query, k=1000):

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    db = PGVector(embeddings=embeddings, collection_name=collection_name, connection=connection)
    
    similar_docs = db.similarity_search_with_score(query=query,k=k)
    return similar_docs

def getContext():
    connection = "postgresql+psycopg://postgres:lovedeep@192.168.1.3:5432/vector_db"
    collection_name = "state_of_the_union_vectors"
    
    query = ("Can you help with the following scenario. We have a campaign on a daily budget of £10. "
             "At 12pm we would put this budget to 2x so effectively this would now be £20 giving it an extra £10. "
             "However if we manually change this budget to another value (say £30), what will happen to the base budget? "
             "As we have changed the budget when it's on 2x, will this affect the base budget? Ideally, we would need the base budget to be reflected in this change to the £15.")
    
    results = similarity_search(connection, collection_name, query)
    print(f"Number of search results: {len(results)}")
    docPage =""
    for doc, score in results:
        print("Document ID:", doc.id)
        print("Source:", doc.metadata['source'])
        print("Content:", doc.page_content)
        print("Similarity Score:", score)
        print("-" * 40)
        if score > 0.7:
            docPage += doc.page_content

        
    return  docPage, query

