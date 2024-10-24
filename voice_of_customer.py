from format_transcripts import GetTranscriptsImplementation
from openai_api import OpenAIRequestImplementation
import json
from ivoice_of_customer import IvoiceOfCustomer

class VoiceOfCustomer(IvoiceOfCustomer):
    systemMessage="From the meeting transcript, find and list all examples of overly positive comments, such as 'Great job' or 'Excellent performance,' and overly negative comments, like 'Terrible outcome' or 'Poor execution.' For each instance, provide the speaker's name and categorize them accordingly."
    max_tokens = 300
    model = "gpt-4o-mini"
    temperature = 0.2
    def get_voice_of_customer(self,org_id, id):
        transcripts= GetTranscriptsImplementation()
        text,token_count,word_count  = transcripts.get_formated_transcripts(org_id, id)
        print(token_count)
        print(word_count)
        if(token_count>30000):
            exit()
        
        messages = [
            {
                "role": "system",
                "content": [
                {
                    "type": "text",
                    "text": self.systemMessage
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
        c = OpenAIRequestImplementation()
        response = c.open_ai_get_request(self.temperature,self.model,self.max_tokens, messages)
        with open('responses.txt', 'a') as file:
            new_line = "---------------------------------------------\n"
            json_response = new_line+ "role : "+response.get("role")+" Temperature : "+str(response.get("temp"))+" Model : "+str(response.get("model"))+'\n'
            json_response = json_response+"content : { "+response.get('content')+" } "+'\n'
            file.write(json_response + '\n \n')  
        return response