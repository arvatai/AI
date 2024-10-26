from abc import ABC, abstractmethod

class GetTranscriptsInterface(ABC):

    @abstractmethod
    def get_formated_transcripts(self, orgID, id):
        pass