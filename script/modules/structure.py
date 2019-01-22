"""Provides a method to get a list of docs/ articles in their correct order."""

from re import search, sub
from os import walk, path, sep


def _build_structure(structure_dict, structure_list):
    """Recursively creates the docs/ structure."""
    for k, v in sorted(structure_dict.items()):
        # either add the path to file to the list or call itself recursively
        if type(v) == str:
            structure_list.append(v)
        elif type(v) == dict:
            _build_structure(v, structure_list)


def get_docs_structure():
    """Returns a list of the .md files in the docs/ folder and its subfolders
    in the correct order."""
    # the dictionary for nesting the files and directories
    structure_dict = {}

    # read through all files in the current folder and all its subfolders
    for root, subdirs, files in walk(\
        path.join(path.dirname(path.realpath(__file__)), "..", "..", "docs")):
        # for ordering topic articles
        topic_structure = {}

        for name in files:
            # information about the file
            file_path = path.join(root, name)
            file_content = open(file_path, 'r').read()
            file_order = int(search("nav_order: ([0-9]+)", file_content).group(1))

            # remove everything before (and including) docs/
            file_path = sub(r"(.+?\.\.[\\\/]docs[\\\/])", "", file_path)

            # if it's a file directly in the docs/ directory
            if file_path.count(sep) == 0:
                structure_dict[file_order] = file_path

            # if it's the main topic article
            elif search(r"(.+)[\\\/]\1\.md", file_path) != None:
                structure_dict[file_order] = topic_structure
                topic_structure[0] = file_path

            # if it's a regular topic article
            else:
                topic_structure[file_order] = file_path

    structure_list = []
    _build_structure(structure_dict, structure_list)

    return structure_list
