import sys
import time

def copy_to_notepad(source_file, destination_file):
    # Read the content of the source file
    with open(source_file, 'r') as f_source:
        content = f_source.read()

    # Write content to the destination file word by word
    with open(destination_file, 'w') as f_destination:
        word = ""
        for char in content:
            if char == " ":
                f_destination.write(word + char)
                f_destination.flush()  # Flush the buffer to save the changes
                word = ""
                time.sleep(0.1)  # Add a small delay
            else:
                word += char
        # Write the last word (without a space at the end)
        if word:
            f_destination.write(word)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <source_file.py> <destination_file.py>")
        sys.exit(1)

    source_file = sys.argv[1]
    destination_file = sys.argv[2]

    copy_to_notepad(source_file, destination_file)
