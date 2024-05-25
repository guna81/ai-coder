from models.gemini import chat
from utils.format_response import remove_codeblock_markers
# from prompt.templates.command_generation import GENERATE_FOLDER_STRUCTURE

def generate_code(prompt):
    print('prompt', prompt)
    response = chat(prompt)
    print('response', response.text)

    result = remove_codeblock_markers(response.text)
    print('raw_text', result)
    return result