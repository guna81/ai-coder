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


def create_file(file_name, parent_dir, file_content):
    # Create the file
    path = os.path.join(OUTPUT_PATH, parent_dir, file_name)
    
    if file_content:
        with open(path, "w") as f:
            f.write(file_content)
    else:
        with open(path, "w") as f:
            pass

    print(f"File '{file_name}' created successfully.")


def create_file_structure(structure, base_path=OUTPUT_PATH):
    if structure["type"] == "folder":
        folder_path = os.path.join(base_path, structure["name"])
        os.makedirs(folder_path, exist_ok=True)
        for child in structure.get("children", []):
            create_file_structure(child, folder_path)
    elif structure["type"] == "file":
        file_path = os.path.join(base_path, structure["name"])
        with open(file_path, 'w') as f:
            pass  # create an empty file


def update_file_content(file_name, content):
    print(file_name)
    path = os.path.join(OUTPUT_PATH, file_name)
    with open(path, "w") as f:
        f.write(content)

    print(f"File '{file_name}' updated successfully.")