from openai import OpenAI
import os
from Iopenai_api import OpenAIRequestInterface


class OpenAIRequestImplementation(OpenAIRequestInterface):

    def open_ai_get_request(self, temperature, model, max_tokens, messages):
        openAiKey = os.getenv('OPENAI_API_KEY')
        client = OpenAI()
        completion = client.chat.completions.create(
            max_tokens=max_tokens,
            model=model,
            temperature=temperature,
            messages=messages
        )

        response_message = completion.choices[0].message

        response_message_dict = {
            "model": model,
            "temp": temperature,
            "role": response_message.role,
            "content": response_message.content
        }
        return response_message_dict