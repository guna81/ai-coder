import json
from main.generator.generator import generate
# from core.generator.command import generate_command
from main.generator.code import generate_code

from const.const import FILE_STRUCTURE_JSON
from prompt.create_prompt import create_prompt, GET_APP_DETAILS, GENERATE_FOLDER_STRUCTURE
from prompt.templates.code_generation import GET_CURRENT_FILE, GENERATE_CODE

from utils.handle_files import create_file_structure, update_file_content
from utils.app_tree import update_file_tree


def create_app(app_name, description, tech_stack):
    print(f"Creating app: {app_name} with description: {description} and tech stack: {tech_stack}")

    context = {
        "name": app_name,
        "description": description,
        "tech_stack": tech_stack,
    }

    app_details = prompt = create_prompt(GET_APP_DETAILS, context)
    
    context = {
        "app_details": app_details,
        "template": FILE_STRUCTURE_JSON
    }
    prompt = create_prompt(GENERATE_FOLDER_STRUCTURE, context)
    
    response =  generate(prompt)
    file_structure = json.loads(response)
    
    # Create the app folders
    create_file_structure(file_structure)
    print("Project folder structure created successfully.")

    # update project folder structure
    update_file_tree(app_name, file_structure)

    development_loop(app_details, file_structure, path=0, file=0)

    print("App created successfully.")


def get_current_file(app_details, file_structure):
    context = {
        "app_details": app_details,
        "file_structure": file_structure
    }
    prompt = create_prompt(GET_CURRENT_FILE, context)

    file_name =  generate(prompt)
    print("current_file", file_name)
    
    return file_name

def get_files_bfs(data):
  """
  Prints each file with its parent path from the root in BFS order.

  Args:
    data: A dictionary representing the file structure.
  """
  result = []

  queue = [(data, "")]  # Queue holds (node, parent_path) tuples

  while queue:
    node, parent_path = queue.pop(0)
    if node["type"] == "file":
      print(f"{parent_path}/{node['name']}")
      result.append(f"{parent_path}/{node['name']}")
    else:
      # Append children with updated parent path
      for child in node["children"]:
        queue.append((child, f"{parent_path}/{node['name']}" if parent_path else node['name']))

  return result

def development_loop(app_details, file_structure, path, file):
    files = get_files_bfs(file_structure)
    
    for current_file in files:
        # generate code
        context = {
            'app_details': app_details,
            "file_structure": file_structure,
            "current_file": current_file.split('/')[-1],
        }
        prompt = create_prompt(GENERATE_CODE, context)

        code =  generate_code(prompt)

        update_file_content(current_file, code)