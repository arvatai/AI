from mongoConnect import get_mongo_client
import re
import json
import tiktoken

uri="mongodb://localhost:27017/"
db_name="gosky"
collection_name="aggregated_transcripts"
def get_documents_by_org_id(org_id,id):
    
    client = get_mongo_client(uri)
    if client is None:
        return None
   
    try:
        db = client[db_name]
        collection = db[collection_name]
        query = {"orgId": org_id,"id":id}
        documents = collection.find_one(query)
        
        return documents

    except Exception as e:
        print(f"An error occurred while retrieving documents: {e}")
        return None

    finally:
        client.close()
def update_document_by_org_id_and_id(org_id, id, new_voice_text):
    client = get_mongo_client(uri)
    if client is None:
        return None
    try:
        db = client[db_name]
        collection = db[collection_name]
        query = {"orgId": org_id, "id": id}
        update = {"$set": {"voice": new_voice_text}}
        result = collection.update_one(query, update)
        
        if result.modified_count > 0:
            return True 
        else:
            return False 
    
    except Exception as e:
        print(f"An error occurred while updating the document: {e}")
        return None
    
    finally:
        client.close()


