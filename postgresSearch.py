import marqo
from langchain.prompts import PromptTemplate
from openai_api import OpenAIRequestImplementation
from huggingface_query import getContext
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

template = """
Given the following extracted part of a long document ("SOURCE") and a question ("QUESTION"), create a final answer one paragraph long.
Don't try to make up an answer and use the text in the SOURCE only for the answer. If you don't know the answer, just say that you don't know.
QUESTION: {question}
=========
SOURCE:
{source}
=========
ANSWER:
"""
context,query = getContext()

prompt = PromptTemplate(template=template, input_variables=["source", "question"])

formatted_prompt = prompt.format(source=context, question=query)
print(context)
chat = OpenAIRequestImplementation()
response = chat.open_ai_get_request(
    temperature=0.5,
    model="gpt-3.5-turbo",
    max_tokens=100,
    messages=[{"role": "user", "content": formatted_prompt}]
)

print(response)
