"""Generates the structure of the docs/ folder.
Used by generate_sitemap.py and generate_tex_file.py."""

from re import search
from os import walk, path, sep

def write_structure(structure, file):
    """Recursively writes the ordered structure of docs/ to a file."""
    for k, v in sorted(structure.items()):
        # either write a path or call itself recursively
        if type(v) == str:
            file.write(v + "\n")
        elif type(v) == dict:
            write_structure(v, file)


# the dictionary for nesting the files and directories
structure_dict = {}

# read through all files in the current folder and all its subfolders
for root, subdirs, files in walk(path.join("..", "docs")):
    # for ordering topic articles
    topic_structure = {}

    for name in files:
        # information about the file
        file_path = path.join(root, name)
        file_content = open(file_path, 'r').read()
        file_order = int(search("nav_order: ([0-9]+)", file_content).group(1))

        # if it's a file directly in the docs/ directory
        if file_path.count(sep) == 2:
            structure_dict[file_order] = file_path

        # if it's the main topic article
        elif search(r"(.+)[\\\/]\1\.", file_path) != None:
            structure_dict[file_order] = topic_structure
            topic_structure[0] = file_path

        # if it's a regular topic article
        else:
            topic_structure[file_order] = file_path


write_structure(structure_dict, open("structure", "w"))