from operator import truediv

import google.generativeai as ai
API_KEY ='ENTER YOUR GEMINI AI API'
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()
chat_over=True
while chat_over:
    message = input('You: ')
    if message.lower() == 'bye':
        print('Chatbot: Goodbye!')
        chat_over=False
    response = chat.send_message(message)
    print('Chatbot:', response.text)
