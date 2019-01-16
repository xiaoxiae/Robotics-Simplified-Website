from regex import sub, match, search, MULTILINE
from datetime import datetime
from os import walk, path, sep, makedirs

# regular expressions and their substitution results
substitutions = [
    ("---\n(.+\n)+---", ""),                            # remove config
    ("^---\n", ""),                                     # remove linebreaks
    ("^Modified *{.+", ""),                             # remove last modified
    ("(^!\[.+?\]\(.+?\))\n(.*?\n)*\[.+\]\(.+\)\n{.+}",\
     "\g<1>"),                                          # remove image sources
    (".+\n*{: *\.fs-6 *\.fw-300 *}", ""),    # remove topic description sentence
    ("\\\\(sub)*section{Visualization}\n(.*\n)+^\\\\",\
     "\\\\"),                                           # remove visualizations
    ("\*\*(.+?)\*\*", "\\\\textbf{\g<1>}"),             # bold text
    ("\*(.+?)\*", "\\\\textit{\g<1>}"),                 # italics
    ("(```python\n){% +include +(.+?) +%}(\n```)",\
        lambda x: x.group(1) + \
        open(path.join("..", "_includes", x.group(2)), "r").read() + \
        x.group(3)),                                    # insert code snippet
    ("```python(\n(.*\n)+?)```",
     "\\\\begin{lstlisting}\g<1>\\\\end{lstlisting}"),  # code highlights
    ("!\[.+\]\({{.+}}(.+) \"(.+)\"\)", \
     "\\\\begin{figure}\n" + \
     "\\\\centering\n" + \
     "\\\\includegraphics[width=0.8\\\\textwidth]{..\g<1>}\n" + \
     "\\\\caption{\g<2>}\n" + \
     "\\\\end{figure}"),
    ("\[(.+?)\]\((.+?)\)", "\\\\href{\g<2>}{\g<1>}"),   # href
    ("(.+?)\$(\$.*?\$)\$(.+?)", "\g<1>\g<2>\g<3>"),     # $$.$$ to $.$
    ("`([^`\n]+?)`","\\\\texttt{\g<1>}"),               # `` md highlights
    ("ttt{[^}]*?_[^{]*?}", lambda x:x.group(0).replace("_", "\\_")), # escape _
    ("ref{[^}]*?%[^{]*?}", lambda x:x.group(0).replace("%", "\\%")), # escape %
    ("^(- .+\n)+", "\\\\begin{itemize}\n\g<0>\\\\end{itemize}"),    # itemize
    ("(^- (.+)\n)+?", "\\\\item \g<2>\n"),              # - to \item
    ("{:.+?}", "")                                      # delete {:...} lines
]

# the groups of converted files
convertedGroups = {}

# read through all of the files
for root, subdirs, files in walk(path.join("..", "docs")):
    #  contents of the converted files
    convertedFiles = {}

    for name in files:
        fPath = path.join(root, name)
        fContent = open(fPath, 'r').read()
        fileOrder = int(search("nav_order: ([0-9]+)", fContent).group(1))

        # if the file is in the form of .../topic/topic.md - the main topic file
        isMainTopic = search(r"(.+)[\\\/]\1\.", fPath) != None

        # the "depth" of the file - how many levels of folders it is in
        fDepth = fPath[8:].count(sep)

        # replace the headings based on the file depth - the further it is in,
        # the more sub will be added in in front of section{...}
        fContent = sub("^(#+) (.+)",\
            lambda x: "\\"\
                + (len(x.group(1)) + fDepth - 1 - int(isMainTopic)) * "sub"\
                + "section{" + x.group(2)\
                + "}",\
            fContent, flags=MULTILINE)

        # run the file through the substitution regexes
        for substitution in substitutions:
            fContent = sub(*substitution, fContent, flags=MULTILINE)

        # if it's at depth 0 by default - files like about.md, preface.md...,
        # convertedGroups[fileOrder] will be the file itself
        if fDepth == 0:
            convertedGroups[fileOrder] = (fContent, fPath)

        # if it's at depth 0 because it is the main topic,
        # convertedGroups[fileOrder] will be the group of files
        elif fDepth - int(isMainTopic) == 0:
            convertedGroups[fileOrder] = convertedFiles

        # add the converted file to the fileOrder position
        convertedFiles[fileOrder if not isMainTopic else 0] = (fContent, fPath)


# the converted latex file
latexOut = open("website.tex", "w")

# write beginning
latexOut.write(open(path.join("tex-generation-files", "beginning"), "r").read())

# write the converted articles in their respective order
for k1, v1 in sorted(convertedGroups.items()):
    if type(v1[0]) == str:
        latexOut.write(v1[0] + "\n")
    else:
        for k2, v2 in sorted(v1.items()):
            latexOut.write(v2[0] + "\n")

# write ending
latexOut.write(open(path.join("tex-generation-files", "ending"), "r").read())


def writeURL(url, subpath, xmlFile, priority = "0.8", lastmod = None):
    """Writes information about a specific URL to the sitemap.xml file."""
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
        xmlFile.write(line + "\n")


# create folder where sitemap should be
if not path.exists(path.join("..", "_site")):
    makedirs(path.join("..", "_site"))

# the generated sitemap
sitemapOut = open(path.join("..", "_site", "sitemap.xml"), "w")

# write beginning
sitemapOut.write(open(path.join("xml-generation-files", "beginning"), "r").read())

# get the url of the website from _config.yml
url = search("^url: \"(.+)\".*\n",\
    open(path.join("..", "_config.yml"), "r").read(), MULTILINE).group(1)

# write information about the main page
writeURL(url, "", sitemapOut, "1.00",\
    datetime.utcfromtimestamp(path.getmtime(path.join("..", "index.md")))\
            .strftime('%Y-%m-%dT%H:%M:%S+00:00'))

# write all of the URLs to the .xml file
for k1, v1 in sorted(convertedGroups.items()):
    if type(v1[1]) == str:
        writeURL(url, v1[1], sitemapOut)
    else:
        for k2, v2 in sorted(v1.items()):
            writeURL(url, v2[1], sitemapOut)

# write ending
sitemapOut.write(open(path.join("xml-generation-files", "ending"), "r").read())

# properly close the files
latexOut.close()
sitemapOut.close()
