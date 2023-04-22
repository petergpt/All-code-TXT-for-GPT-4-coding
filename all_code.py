import os

def is_code_file(filename):
    return filename.endswith('.py') or filename.endswith('.html') or filename.endswith('.css')

def get_all_files(path):
    all_files = []
    for root, _, files in os.walk(path):
        # Skip directories you don't want to include (e.g., 'venv')
        if 'venv' in root:
            continue

        for file in files:
            if is_code_file(file):
                all_files.append(os.path.join(root, file))
    return all_files

# Get the path of the current directory
current_dir = os.getcwd()

# Get a list of all the code files in the directory and its subdirectories
code_files = get_all_files(current_dir)

# Combine all the code files into a single file called 'all_code.txt'
with open('all_code.txt', 'w') as outfile:
    # Add the specified text as the first line in the file
    outfile.write("Here's all of my code, please review and tell me what it is doing so I can make sure that you understand it. Ask me any clarifying questions if needed.\n\n")

    for fname in code_files:
        with open(fname) as infile:
            outfile.write(f"----- Start of {fname} -----\n")
            outfile.write(infile.read())
            outfile.write(f"\n----- End of {fname} -----\n\n")

# Notify the user that the file has been created
print('The file "all_code.txt" has been created!')