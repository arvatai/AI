
from get_transcripts import get_documents_by_org_id
import os
import tiktoken
def read_and_clean_file(file_path):
  
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        os.remove(file_path)
        return content

    except FileNotFoundError:
        
        return None
    except Exception as e:
        
        return None

def chunk_text(text, word_limit=2000):
 
    words = text.split() 
    chunks = [' '.join(words[i:i + word_limit]) for i in range(0, len(words), word_limit)]
    return chunks

def count_tokens(text):
    
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    return len(encoding.encode(text))

def count_words(text):
    
    return len(text.split())



def get_formated_transcripts(orgID,id):
    documents = get_documents_by_org_id(orgID,id)
    fileName= id+".txt"
    if documents:
        sentences = documents.get("sentences")

        if sentences:
            raw_data = ""
            for sentence in sentences:
                speaker_name = sentence.get("speaker_name", "")
                raw_text = sentence.get("raw_text", "")
                raw_data += f"{speaker_name} {raw_text}\n"
            token_count = count_tokens(raw_data)
            word_count = count_words(raw_data)

            print(f"GPT Token Count: {token_count}")
            print(f"Word Count: {word_count}")
            
            with open(fileName, 'w') as file:
                file.write(raw_data)
            return fileName , token_count, word_count
            
        else:
            return False, False, False
    else:
        return False, False, False