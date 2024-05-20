from models.gemini import chat
from utils.execute_command import run_command
from utils.clean_response import clean_response
from prompt_templates.commands import EXECUTE_PYTHON_FILE

# get pwd using function


file_name = "generated_files/response.py"

# prompt = """
# folder_name = "generated_files"
# """

response = chat(file_name + EXECUTE_PYTHON_FILE)

print('response', response.text)
# print('history', chat_session.history)

result = clean_response(response.text)
run_command(result)

# store the command if needed