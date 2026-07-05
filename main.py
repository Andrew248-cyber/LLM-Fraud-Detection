from openai import OpenAI
import json
import os
client = OpenAI(api_key= os.getenv('OPENAI_API_KEY')) #Adding and incorporating OpenAPI Key 
def tag_email():
        input_email = {'to': 'adaniel2023@fau.edu', 'from': '<prime@amazon.com>', 'subject': 'Billion Dollar prize',
               'message': "Congrats!!!!! you have just won a BILLION DOLLARS!!!!! Please click the link IMMEDIATELY to claim your prize. "
               "If you don't, you will NOT receive your money! http://"} #Email for GPT to analyze
AI_model = client.chat.completions.create(model="gpt-4o-mini", messages=[{'role': 'user', 
        'content': 'Analyze the email above and return a scam score out of 100 as a JSON object in the form "result" and '
        'explain why the email is a scam in the form "evidence"'}], #Prompt for gpt-4o-mini to analyze
          response_format={'type': 'json_object'})
result = json.loads(AI_model.choices[0].message.content) #Efficient way of loading and printing a JSON output
print(result['result'])
print(result['evidence']) 
#Citations for AI code: json.loads, "result" and "evidence" keys, response_format, print(result['result]) and print(result['evidence])
#"Microsoft Copilot. Accessed 2025-12-10. Prompt #1: How to incorporate API Key into Python. Prompt #2: Please Explain the Errors in my Code: Code. 
#Generated using https://copilot.microsoft.com/