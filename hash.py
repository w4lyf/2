import hashlib

file_path = input("Enter the path to the file: ")

try:
    
    with open(file_path, 'rb') as f:
        
        chunk_size = 4096
        hasher = hashlib.sha256()
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            hasher.update(data)
    
    print("The SHA-256 hash of the file is:", hasher.hexdigest())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to access the file.")
except Exception as e:
    print("An error occurred:", e)
