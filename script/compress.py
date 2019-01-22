from os import path, walk
from modules.crypto import decrypt
from getpass import getpass
import tinify

# an AES-encrypted API token
encrypted_key = b'gAAAAABcR2VvBRCEWDErzAvN6JJz3UHrQlly0N9-FUx58kY366Tt8K89JyA8b8lvLJVx0-46LSR3Z2Pc7w8ho_XHKIa8PtL7HBYv9Uz3HyrpAiD8rcGODA8KzY_3pX-wiDv5KsBRKfj7'
decrypted_key = None

# repeatedly attempt to decrypt until it works
while decrypted_key == None:
    decrypted_key = decrypt(bytes(getpass("AES key: "), "utf-8"), encrypted_key)

# tinify key is the decrypted decoded API token
tinify.key = decrypted_key.decode("utf-8")

# recursively find all of the images in the root folder and all its subfolders
for root, subdirs, files in walk("../_site/assets/images"):
    for file in files:
        if file.endswith(("png", "jpg")):
            file_path = path.join(root, file)

            # compress files larger than 100 KB
            if path.getsize(file_path) / 1024 > 100:
                # tinify the image
                source = tinify.from_file(file_path)
                source.to_file(file_path)