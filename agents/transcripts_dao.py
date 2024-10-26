from mongo_connection import MongoConnection

from itranscripts_dao import ITranscriptsDAO

class TranscriptsDAO(ITranscriptsDAO):
    uri="mongodb://localhost:27017/"
    db_name="gosky"
    collection_name="aggregated_transcripts"
    def get_documents_by_org_id(self,org_id,id):
        c = MongoConnection()
        client = c.get_mongo_client(self.uri)
        if client is None:
            return None
    
        try:
            db = client[self.db_name]
            collection = db[self.collection_name]
            query = {"orgId": org_id,"id":id}
            documents = collection.find_one(query)
            
            return documents

        except Exception as e:
            print(f"An error occurred while retrieving documents: {e}")
            return None

        finally:
            client.close()
    def update_document_by_org_id_and_id(self,org_id, id, new_voice_text):
        c = MongoConnection()
        client = c.get_mongo_client()
        if client is None:
            return None
        try:
            db = client[self.db_name]
            collection = db[self.collection_name]
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


