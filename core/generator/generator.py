from models.gemini import chat
from utils.format_response import markdown_to_text
# from prompt.templates.command_generation import GENERATE_FOLDER_STRUCTURE

def generate(prompt):
    print('prompt', prompt)
    response = chat(prompt)
    print('response', response.text)

    result = markdown_to_text(response.text)
    print('raw_text', result)
    return result