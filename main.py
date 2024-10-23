from clean_transformations import get_formated_transcripts,read_and_clean_file
from openAIApiTest import get_voice_of_customer
import json

fileName,token_count,word_count = get_formated_transcripts("66ee6885d74a544e1691a641", "2ecZKPhADVim46zb")
print(fileName)
print(token_count)
print(word_count)

if(token_count>30000):
    exit()
text = read_and_clean_file(fileName)
response = get_voice_of_customer(text)
with open('responses.txt', 'a') as file:
    new_line = "---------------------------------------------\n"
    json_response = new_line+ "role : "+response.get("role")+'\n'
    json_response = json_response+"content : { "+response.get('content')+" } "+'\n'
    file.write(json_response + '\n \n')  
