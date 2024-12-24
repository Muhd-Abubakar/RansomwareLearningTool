import os  # Import the os module for interacting with the operating system
from cryptography.fernet import Fernet  # Import Fernet for encryption and decryption

# Initialize an empty list to hold the names of files to be decrypted
files = []

# Loop through all items in the current directory
for file in os.listdir():
    # Skip the main script and key file to avoid processing them
    if file == "main.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    # Check if the item is a file and add it to the files list
    if os.path.isfile(file):
        files.append(file)

# Open the key file to read the secret key used for decryption
with open("thekey.key", "rb") as thekey:
    secretKey = thekey.read()  # Read the secret key from the file

# Loop through each file that needs to be decrypted
for file in files:
    # Open the file in binary read mode
    with open(file, "rb") as f:
        file_data = f.read()  # Read the encrypted file data

    # Decrypt the file data using the secret key
    decrypt_data = Fernet(secretKey).decrypt(file_data)

    # Open the file in binary write mode to overwrite it with decrypted data
    with open(file, "wb") as f:
        f.write(decrypt_data)  # Write the decrypted data back to the file