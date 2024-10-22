from mongoConnect import get_mongo_client
import re
import json
import tiktoken

#TODO
#make everything parametriezed from the python cli. example: orgID, transcriptID
#temperature
#max tokens
#imporve code
#chunk


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

def count_tokens(text):
    # Use the encoding for GPT-3 (or choose the correct encoding for the model you're using)
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    return len(encoding.encode(text))

def count_words(text):
    # Split by whitespace to count words
    return len(text.split())

if __name__ == "__main__":
    documents = get_documents_by_org_id("668f523a28251c636bafea0c", "gosky", "aggregated_transcripts", "2ecZKPhADVim46zb")
    
    if documents:
        # Retrieve the sentences from the documents
        sentences = documents.get("sentences")

        if sentences:
            raw_data = ""
            for sentence in sentences:
                speaker_name = sentence.get("speaker_name", "")
                raw_text = sentence.get("raw_text", "")
                raw_data += f"{speaker_name} {raw_text}\n"
            
            # Calculate and print the token count and word count
            token_count = count_tokens(raw_data)
            word_count = count_words(raw_data)

            print(f"GPT Token Count: {token_count}")
            print(f"Word Count: {word_count}")
            
            # Write the result to a file
            with open("hi.txt", 'w') as file:
                file.write(raw_data)
        else:
            print("No sentences found in the document.")
    else:
        print("No documents found or an error occurred.")


def read_and_clean_file(file_path):
  
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
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