from abc import ABC, abstractmethod


class ITranscriptsDAO(ABC):
    
        @abstractmethod
        def get_documents_by_org_id(self,org_id,id):
            pass
    

        @abstractmethod
        def update_document_by_org_id_and_id(self,org_id, id, new_voice_text):
            pass
