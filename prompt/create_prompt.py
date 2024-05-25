from .templates.generic import *
# from .templates.command_generation import *
# from .templates.code_generation import *

def create_prompt(prompt, context):
    args = list(context.values())
    prompt = prompt.format(*args)
    prompt = prompt + "\n" + GENERATE_SCRIPT
    return prompt