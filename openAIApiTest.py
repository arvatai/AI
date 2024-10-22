from openai import OpenAI
from get_transcripts import read_and_clean_file 
import os
import json
openAiKey = os.getenv('OPENAI_API_KEY')
client = OpenAI()
text  = read_and_clean_file("hi.txt")
aboutUser= "GoX.ai is a fast paced SaaS Product company located in Chennai that builds tools for marketers to simplify their work with data automation"

completion = client.chat.completions.create(
    model="gpt-4o",
    messages= [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "From the meeting transcript, find and list all examples of overly positive comments, such as 'Great job' or 'Excellent performance,' and overly negative comments, like 'Terrible outcome' or 'Poor execution.' For each instance, provide the speaker's name and categorize them accordingly."
        }
      ]
    },
    # {
    #   "role": "assistant",
    #   "content": [
    #     {
    #       "type": "text",
    #       "text": "ask About the client's background"
    #     }
    #   ]
    # },
    # {
    #   "role": "user",
    #   "content": [
    #     {
    #       "type": "text",
    #       "text": "client name is GOX AI and my company is ARVAT AI about out client "+aboutUser
    #     }
    #   ]
    # },
    # {
    #   "role": "assistant",
    #   "content": [
    #     {
    #       "type": "text",
    #       "text": "ask for meeting transcript"
    #     }
    #   ]
    # },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": text
        }
      ]
    }
  ]
)

# Extract the response message
response_message = completion.choices[0].message

# Convert to a dictionary and pretty print the JSON
response_message_dict = {
    "role": response_message.role,
    "content": response_message.content
}

# Pretty print the JSON
print("Response in JSON format:\n")
print(json.dumps(response_message_dict, indent=4))