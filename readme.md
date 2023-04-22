# Code TXT for GPT-4 Coding

## Overview

Limited context window is a constant issue with using GPT-4 for coding. This Python script gets all of your code into a single text file that can be easily copy-pasted into a new GPT-4 playground window to make it easier to start a new session with a fresh context window.

The script searches for Python, HTML, and CSS files in the current directory and its subdirectories, and then combines the content of all these files into a single text file named `all_code.txt`. This makes it easier to share your code with GPT-4 without worrying about the context window limitations.

## How to Use

1. Download or clone this repository to your local machine.

2. Open the project folder in your preferred code editor or IDE.

3. (Optional) Modify the `all_code.py` script to include or exclude specific file types or directories as needed. You can copy-paste the code to GPT-4 if you have some other requirements (e.g. file formats)

4. Open a terminal or command prompt in the project directory.

5. Run the script by typing the following command in the terminal or command prompt:

   ```
   python all_code.py
   ```
   
7. The script will execute, and the terminal or command prompt will display the message "The file `all_code.txt` has been created!" upon successful completion.

8. You should now see a new file named `all_code.txt` in your project directory, containing your combined code.

9. Copy the content of the `all_code.txt` file and paste it into a new GPT-4 Playground window to continue your coding session with GPT-4.