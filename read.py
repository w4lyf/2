
file_path = input("Enter the path to the file: ")

try:
    
    with open(file_path, 'r') as file:
        
        lines = file.readlines()
    
    print("Contents of the file:")
    for line in lines:
        print(line.strip())  
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to access the file.")
except Exception as e:
    print("An error occurred:", e)
