from models.gemini import chat
from utils.execute_command import run_command
from utils.format_response import clean_response
# from prompt.templates.command_generation import GENERATE_FOLDER_STRUCTURE

def generate_command(prompt):
    prompt = prompt
    response = chat(prompt)

    print('response', response.text)
    # print('history', chat_session.history)

    result = clean_response(response.text)
    # run_command(result)

    # store the command if needed

    return result