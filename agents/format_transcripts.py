
from transcripts_dao import TranscriptsDAO
from iformat_transcripts import GetTranscriptsInterface
import os
import tiktoken

class GetTranscriptsImplementation(GetTranscriptsInterface):
    
    def chunk_text(self, text, word_limit=2000):
        words = text.split() 
        chunks = [' '.join(words[i:i + word_limit]) for i in range(0, len(words), word_limit)]
        return chunks

    def count_tokens(self, text):
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        return len(encoding.encode(text))

    def count_words(self, text):
        return len(text.split())

    def get_formated_transcripts(self, orgID, id):
        c = TranscriptsDAO()
        documents = c.get_documents_by_org_id(orgID, id)
        
        if documents:
            sentences = documents.get("sentences")

            if sentences:
                raw_data = ""
                for sentence in sentences:
                    speaker_name = sentence.get("speaker_name", "")
                    raw_text = sentence.get("raw_text", "")
                    raw_data += f"{speaker_name}: {raw_text}\n" 

                # Using self to call instance methods
                token_count = self.count_tokens(raw_data)
                word_count = self.count_words(raw_data)

                print(f"GPT Token Count: {token_count}")
                print(f"Word Count: {word_count}")

                return raw_data, token_count, word_count
                
            else:
                return False, False, False
        else:
            return False, False, False
