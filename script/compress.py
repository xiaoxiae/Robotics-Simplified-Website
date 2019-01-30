"""Compresses website's images using TingPNG API for Python."""

from os import path, walk
from modules.crypto import decrypt
from getpass import getpass
import tinify

# an AES-encrypted API token
encrypted_key = b'gAAAAABcR2VvBRCEWDErzAvN6JJz3UHrQlly0N9-FUx58kY366Tt8K89JyA8b8lvLJVx0-46LSR3Z2Pc7w8ho_XHKIa8PtL7HBYv9Uz3HyrpAiD8rcGODA8KzY_3pX-wiDv5KsBRKfj7'
decrypted_key = None

# repeatedly attempt to decrypt until it works
while decrypted_key == None:
    decrypted_key = decrypt(\
        bytes(getpass("Input TinyPNG token password: "), "utf-8"),\
        encrypted_key)

# tinify key is the decrypted decoded API token
tinify.key = decrypted_key.decode("utf-8")

# variables for comparing sizes (before x after)
size_before = 0
size_after = 0

# recursively find all of the images in the root folder and all its subfolders
for root, subdirs, files in walk(path.join("..", "_site", "assets", "images")):
    for file in files:
        if file.endswith(("png", "jpg")):
            file_path = path.join(root, file)
            size_before += path.getsize(file_path)

            print("Compressing " + file_path)

            # tinify the image
            source = tinify.from_file(file_path)
            source.to_file(file_path)

            size_after += path.getsize(file_path)

print("Image compression rate: "\
      + str(round(size_after / size_before * 100, 2)) + "%, "\
      + "saved " + str(round((size_before - size_after) / 1024, 2)) + " KB")
