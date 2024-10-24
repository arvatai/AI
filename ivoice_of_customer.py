from abc import ABC, abstractmethod

class IvoiceOfCustomer(ABC):
    
    @abstractmethod
    def get_voice_of_customer(self,org_id, id):
        pass
    