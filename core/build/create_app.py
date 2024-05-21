import json
from core.generator.command import generate_command
from core.generator.generator import generate

from prompt.create_prompt import create_prompt, GENERATE_FOLDER_STRUCTURE

from utils.create import create_folder_structure

def create_app(app_name, description, tech_stack):
    print(f"Creating app: {app_name} with description: {description} and tech stack: {tech_stack}")

    context = {
        app_name: app_name,
        description: description,
        tech_stack: tech_stack
    }

    # Create the app folders
    prompt = create_prompt(GENERATE_FOLDER_STRUCTURE, context)
    response =  generate(prompt)
    create_folder_structure(json.loads(response))


    # update project folder structure

    