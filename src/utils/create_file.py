import os

folder_name = "generated_files"

def create_file(file_name, content=""):
    # Define filename and path (optional)
    filename = os.path.join(folder_name, file_name)

    # Create the directory if it doesn't exist (optional)
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # Creates "custom_folder" if needed

    # Open the file in write mode ('w')
    with open(filename, 'w') as f:
        # Write your Python code here
        f.write(content)

        print(f"Python script created: {filename}")


