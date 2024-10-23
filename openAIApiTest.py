from openai import OpenAI
system_message = "From the meeting transcript, find and list all examples of overly positive comments, such as 'Great job' or 'Excellent performance,' and overly negative comments, like 'Terrible outcome' or 'Poor execution.' For each instance, provide the speaker's name and categorize them accordingly."

def get_voice_of_customer(text):
  client = OpenAI()
  completion = client.chat.completions.create(
      max_tokens=500,
      model="gpt-4o",
      temperature=0.2,
      messages= [
      {
        "role": "system",
        "content": [
          {
            "type": "text",
            "text": system_message
          }
        ]
      },
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

  response_message = completion.choices[0].message

  response_message_dict = {
      "role": response_message.role,
      "content": response_message.content
  }
  return (response_message_dict)