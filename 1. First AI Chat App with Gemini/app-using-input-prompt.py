import os
from google import genai

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

chat = client.chats.create(model='gemini-2.5-flash')

x = True
while x:
    prompt = input("Enter Prompt: ")
    
    response = chat.send_message(prompt)
    
    print(response.text)
    
