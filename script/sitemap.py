"""Generates a sitemap.xml file for the website."""

from regex import sub, search, MULTILINE
from datetime import datetime
from os import path, makedirs
from modules.structure import get_docs_structure


def writeURL(url, subpath, file, lastmod = None):
    """Writes information about a specific URL to a file."""
    # converts the file subpath to a website path
    converted_subpath = subpath.replace(".md", "/")[8:].replace("\\", "/")

    # if it's the main topic article, remove the repeating name
    converted_subpath = sub(r"(.+)\/\1\/$", "\g<1>/", converted_subpath)

    # priority is the deeper the page is
    priority = str(1.0 - converted_subpath.count("/") * 0.2)

    # creates the url
    address = url + "/" + converted_subpath

    # if lastmod wasn't specified, generate it from the path
    if lastmod == None:
        lastmod = (datetime\
            .utcfromtimestamp(path.getmtime(subpath))\
            .strftime('%Y-%m-%dT%H:%M:%S+00:00'))

    # the contents of the xml record, in a list
    contents = ["<url>",
                "\t<loc>" + address + "</loc>",
                "\t<lastmod>" + lastmod + "</lastmod>",
                "\t<priority>" + priority + "</priority>",
                "</url>"]

    for line in contents:
        file.write(line + "\n")


# create folder where sitemap.xml will be
if not path.exists(path.join("..", "_site")):
    makedirs(path.join("..", "_site"))

# open the file and write the beginning
sitemap = open(path.join("..", "_site", "sitemap.xml"), "w")
sitemap.write(open(path.join("genfiles", "beginning.xml"), "r").read())

# get the url of the website from _config.yml
url = search("^url: \"(.+)\".*\n",\
    open(path.join("..", "_config.yml"), "r").read(), MULTILINE).group(1)

# write information about the main page
writeURL(url, "", sitemap,\
    datetime.utcfromtimestamp(path.getmtime(path.join("..", "index.md")))\
            .strftime('%Y-%m-%dT%H:%M:%S+00:00'))

# write each article in docs/
for subpath in get_docs_structure():
    writeURL(url, path.join("..", "docs", subpath), sitemap)

# write the ending and close the file
sitemap.write(open(path.join("genfiles", "ending.xml"), "r").read())
sitemap.close()
