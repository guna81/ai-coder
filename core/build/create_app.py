import json
from core.generator.command import generate_command
from core.generator.generator import generate
from const.const import FILE_STRUCTURE_JSON
from prompt.create_prompt import create_prompt, GENERATE_FOLDER_STRUCTURE

from utils.create_files import create_file_structure
from utils.app_tree import update_file_tree

def create_app(app_name, description, tech_stack):
    print(f"Creating app: {app_name} with description: {description} and tech stack: {tech_stack}")

    context = {
        "app_name": app_name,
        "description": description,
        "tech_stack": tech_stack,
        "template": FILE_STRUCTURE_JSON
    }

    prompt = create_prompt(GENERATE_FOLDER_STRUCTURE, context)
    response =  generate(prompt)
    files_json = json.loads(response)
    
    # Create the app folders
    create_file_structure(files_json)

    # update project folder structure
    update_file_tree(files_json)