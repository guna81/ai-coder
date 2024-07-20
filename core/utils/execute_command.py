import subprocess

def run_command(command):
    print(command)
    # Define the command to run
    command = command.split(" ")
    # Run the command and capture the output
    process = subprocess.run(command, capture_output=True, text=True)

    # Check the return code (0 for success)
    if process.returncode == 0:
        # Print the captured output
        print(process.stdout)
    else:
        print(f"Error running command: {process.stderr}")


# run_command(["ls", "-l"])