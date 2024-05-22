from models.gemini import chat
from utils.create_files import create_file
from utils.format_response import clean_response
from prompt.templates.code_generation import GENERATE_PYTHON_CODE


def generate_code(prompt):
    response = chat(prompt)

    print('response', response.text)

    result = clean_response(response.text)
    create_file('response.py', result)

