from langchain_openai import OpenAIEmbeddings
from langchain_postgres.vectorstores import PGVector

def similarity_search(api_key, connection, collection_name, query, k=1000):

    embeddings = OpenAIEmbeddings(api_key=api_key)
    db = PGVector(embeddings=embeddings, collection_name=collection_name, connection=connection)

    similar_docs = db.similarity_search_with_score(query=query, k=k)
    return similar_docs

if __name__ == "__main__":
    api_key = "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"
    connection = "postgresql+psycopg://postgres:lovedeep@192.168.1.3:5432/vector_db"
    collection_name = "state_of_the_union_vectors"
    
    query = ("Can you help with the following scenario. We have a campaign on a daily budget of £10. "
             "At 12pm we would put this budget to 2x so effectively this would now be £20 giving it an extra £10. "
             "However if we manually change this budget to another value (say £30), what will happen to the base budget? "
             "As we have changed the budget when it's on 2x, will this affect the base budget? Ideally, we would need the base budget to be reflected in this change to the £15.")

    results = similarity_search(api_key, connection, collection_name, query)
    print(f"Number of search results: {len(results)}")
    for doc, score in results:
        print("Document ID:", doc.id)
        print("Source:", doc.metadata['source'])
        print("Content:", doc.page_content)
        print("Similarity Score:", score)
        print("-" * 40)
