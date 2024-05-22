import os
from const.const import OUTPUT_PATH

def create_folder(folder_name, parent_dir):
    # Create the directory
    path = os.path.join(OUTPUT_PATH, parent_dir, folder_name)
    try:
        os.mkdir(path)
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")
        return

    print(f"Folder '{folder_name}' created successfully.")


def create_file(file_name, content, parent_dir):
    # Create the file
    path = os.path.join(OUTPUT_PATH, parent_dir, file_name)
    
    if content:
        with open(path, "w") as f:
            f.write(content)
    else:
        with open(path, "w") as f:
            pass

    print(f"File '{file_name}' created successfully.")


def create_file_structure(folder_structure, parent_dir=""):
  """
  This function recursively creates a folder structure based on the provided JSON data.

  Args:
      folder_structure: The JSON data representing the folder structure.
      parent_dir: The parent directory path (defaults to an empty string).
  """

  # Process each item in the folder structure
  for item in folder_structure["children"]:
    name = item["name"]
    # Check the type
    if item["type"] == "folder":
      # Create a subfolder
      new_parent_dir = os.path.join(parent_dir, name)
      create_folder(name, parent_dir)
      create_file_structure(item, new_parent_dir)  # Recursive call
    elif item["type"] == "file":
      # Create a file with content (if provided)
      file_path = os.path.join(parent_dir, name)
      file_content = item.get("content", None)  # Get content if it exists, otherwise None
      create_file(name, file_content, parent_dir)
    else:
      print(f"Warning: Unknown item type '{item['type']}' for '{name}'.")


    print("File structure created successfully.")