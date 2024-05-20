from models.gemini import chat
from utils.create_file import create_file
from utils.clean_response import clean_response
from promp_template import CODE_GENERATION

sample_prompt = "generate me a python without any boilerplates or comments anything"

prompt = input("prompt: ")
response = chat(prompt + CODE_GENERATION)

print('response', response.text)
# print('history', chat_session.history)

result = clean_response(response.text)
create_file('response.py', result)

