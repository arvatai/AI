from mongoConnect import get_mongo_client
import re
def get_documents_by_org_id(org_id, db_name, collection_name,id, uri="mongodb://localhost:27017/"):
   
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

if __name__ == "__main__":

    documents = get_documents_by_org_id("66ee6885d74a544e1691a641", "gosky", "aggregated_transcripts","2ecZKPhADVim46zb")
    with open("hi.txt", 'w') as file:
        file.write(str(documents.get("sentences")))
    if documents:
        transcript= documents.get("sentences")
        print(transcript)
    else:
        print("No documents found or an error occurred.")


def read_and_clean_file(file_path):
  
    try:
        with open(file_path, 'r') as file:
            content = file.read()

  
        cleaned_content = re.sub(r'[^\w\s]', '', content)

        return cleaned_content
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def chunk_text(text, word_limit=2000):
 
    words = text.split() 
    chunks = [' '.join(words[i:i + word_limit]) for i in range(0, len(words), word_limit)]
    return chunks