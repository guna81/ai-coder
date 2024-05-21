import os
from const.const import OUTPUT_PATH


def create_folder(folder_name, parent_dir):
    # Create the directory
    path = os.path.join(OUTPUT_PATH, parent_dir, folder_name)
    os.mkdir(path)

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


# def create_folder_structure(json_data, parent_dir=OUTPUT_PATH):
#     print('folder', json_data)
#     for folder in json_data["folders"]:
#         create_folder(folder["name"], parent_dir)

#     for file in json_data["files"]:
#         create_file(file["name"], file["content"], parent_dir)


def create_folder_structure(json_data, base_dir=OUTPUT_PATH):
  """
  Creates a folder structure and files based on the provided JSON data.

  Args:
      json_data (dict): The JSON data representing the desired folder structure.
      base_dir (str): The base directory where the structure will be created.
  """
  for key, value in json_data.items():
    # Create the current folder
    current_path = os.path.join(base_dir, key)
    if os.path.isdir(current_path):
      print(f"Folder '{key}' already exists, skipping creation.")
    else:
      os.makedirs(current_path)
      print(f"Created folder: {current_path}")

    # Check if it's a file (empty string value) or a nested folder structure
    if isinstance(value, str) and value == "":
      # Create an empty file
      file_path = os.path.join(current_path, key + ".js")  # Assuming all files are .js
      with open(file_path, "w") as f:
        f.write("")
      print(f"Created file: {file_path}")
    else:
      # Recursively call the function for nested folders
      create_folder_structure(value, current_path)