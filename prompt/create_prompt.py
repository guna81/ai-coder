from .templates.generic import *
# from .templates.command_generation import *
# from .templates.code_generation import *

def create_prompt(prompt, context):
    prompt = prompt.format(*context)
    prompt = prompt + "\n" + GENERATE_SCRIPT
    return prompt