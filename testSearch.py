import marqo
from langchain.prompts import PromptTemplate
from openai_api import OpenAIRequestImplementation

mq = marqo.Client(url='http://192.168.1.3:8882')
index_name = "my-first-index"

query = "Can you help with the following scenario. We have a campaign on a daily budget of £10. At 12pm we would put this budget to 2x so effectively this would now be £20 giving it an extra £10. However if we manually change this budget to another value (say £30), what will happen to the base budget? As we have changed the budget when it's on 2x, will this affect the base budget? Ideally, we would need the base budget to be reflected in this change to the £15."

results = mq.index(index_name).search(q=query)

print(f"Number of search results: {len(results['hits'])}")

best_result = results['hits'][0]  

print(f"Best Result - Document ID: {best_result['_id']}, Score: {best_result['_score']}, Text: {best_result['text']}")

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

prompt = PromptTemplate(template=template, input_variables=["source", "question"])

formatted_prompt = prompt.format(source=best_result["text"], question=query)

chat = OpenAIRequestImplementation()
response = chat.open_ai_get_request(
    temperature=0.5,
    model="gpt-3.5-turbo",
    max_tokens=100,
    messages=[{"role": "user", "content": formatted_prompt}]
)

print(response)
