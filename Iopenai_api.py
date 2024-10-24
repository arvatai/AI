from abc import ABC, abstractmethod


class OpenAIRequestInterface(ABC):

    @abstractmethod
    def open_ai_get_request(self, temperature, model, max_tokens, messages):
        pass