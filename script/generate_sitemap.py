"""Generates a sitemap.xml file for the website."""

from regex import sub, search, MULTILINE
from datetime import datetime
from os import path, makedirs


def writeURL(url, subpath, file, priority = "0.8", lastmod = None):
    """Writes information about a specific URL to a file."""
    # creates the url
    address = url + "/" + subpath.replace(".md", "/")[8:].replace("\\", "/")

    # if it's the main topic article, remove the repeating name
    address = sub(r"\/(.+)\/\1\/$", "/\g<1>/", address)

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
sitemap.write(open(path.join("xml-generation-files", "beginning"), "r").read())

# get the url of the website from _config.yml
url = search("^url: \"(.+)\".*\n",\
    open(path.join("..", "_config.yml"), "r").read(), MULTILINE).group(1)

# write information about the main page
writeURL(url, "", sitemap, "1.00",\
    datetime.utcfromtimestamp(path.getmtime(path.join("..", "index.md")))\
            .strftime('%Y-%m-%dT%H:%M:%S+00:00'))

# write each article in docs/
for subpath in open('structure', 'r').read().splitlines():
    writeURL(url, subpath, sitemap)

# write the ending and close the file
sitemap.write(open(path.join("xml-generation-files", "ending"), "r").read())
sitemap.close()
