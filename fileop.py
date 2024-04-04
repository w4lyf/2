def create_file(filename):
    try:
        with open(filename, 'w'):
            print(f"File '{filename}' created successfully.")
    except IOError:
        print(f"Error: Unable to create file '{filename}'.")

def write_content(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print("Content written to the file successfully.")
    except IOError:
        print(f"Error: Unable to write to file '{filename}'.")

def read_content(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("Content of the file:")
            print(content)
    except IOError:
        print(f"Error: Unable to read file '{filename}'.")

def append_content(filename, additional_content):
    try:
        with open(filename, 'a') as file:
            file.write(additional_content)
            print("Additional content appended to the file successfully.")
    except IOError:
        print(f"Error: Unable to append to file '{filename}'.")

def delete_file(filename):
    try:
        import os
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except OSError:
        print(f"Error: Unable to delete file '{filename}'.")

def show_menu():
    print("\nMenu:")
    print("1. Create new file")
    print("2. Write content to file")
    print("3. Read file")
    print("4. Append content to file")
    print("5. Delete file")
    print("6. Exit")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter the filename: ")
            create_file(filename)
        elif choice == '2':
            filename = input("Enter the filename: ")
            content = input("Enter the content to write: ")
            write_content(filename, content)
        elif choice == '3':
            filename = input("Enter the filename: ")
            read_content(filename)
        elif choice == '4':
            filename = input("Enter the filename: ")
            additional_content = input("Enter the additional content to append: ")
            append_content(filename, additional_content)
        elif choice == '5':
            filename = input("Enter the filename: ")
            delete_file(filename)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
