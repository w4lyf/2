import sys
import os

def copy_file_contents_to_clipboard(file_path):
    try:
        # Read file contents using PowerShell and copy to clipboard
        os.system(f'powershell -command "& {{(Get-Content \'{file_path}\') | Set-Clipboard}}"')
        print(f"Contents of '{file_path}' copied to clipboard.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python copier.py <file_path>")
    else:
        file_path = sys.argv[1]
        copy_file_contents_to_clipboard(file_path)
