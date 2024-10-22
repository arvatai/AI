from openai import OpenAI
from get_transcripts import read_and_clean_file,chunk_text 
import os
openAiKey = os.getenv('OPENAI_API_KEY')
client = OpenAI()
text  = read_and_clean_file("hi.txt")
chunks = chunk_text(text)
chunk = chunks[0]
aboutUser= "GoX.ai is a fast paced SaaS Product company located in Chennai that builds tools for marketers to simplify their work with data automation"

completion = client.chat.completions.create(
    model="gpt-4o",
    messages= [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "You are a helpful assistant that will take ask about the client's background and then use take transcript to give voice of client while keeping in mind the client's background."
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "ask About the client's background"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "client name is GOX AI and my company is ARVAT AI about out client "+aboutUser
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "ask for meeting transcript"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": chunk
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": chunk[1]
        }
      ]
    }
  ]
)

print(completion.choices[0].message)