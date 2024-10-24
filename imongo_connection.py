from abc import ABC, abstractmethod

class IMongoConnection(ABC):
        
        @abstractmethod
        def get_mongo_client(self,uri):
            pass