from re import sub, match, search, MULTILINE
import os

# regular expressions and their substitution results
subRegex = [
    ("---\n(.+\n)+---", ""),                            # remove config
    ("^---\n", ""),                                     # remove linebreaks
    ("#+ Visualization\n(.*\n)+#", "#"),                # remove visualizations
    ("```python(\n(.*\n)+?)```",
     "\\\\begin{lstlisting}\g<1>\\\\end{lstlisting}"),  # code highlights
    ("\*\*(.+?)\*\*", "\\\\textbf{\g<1>}"),             # bold text
    ("\*(.+?)\*", "\\\\textit{\g<1>}"),                 # * italics
    ("!\[.+\]\({{.+}}(.+) \"(.+)\"\)", \
     "\\\\begin{figure}\n\
      \\\\centering\n\
      \\\\includegraphics[width=0.8\\\\textwidth]{..\g<1>}\n\
      \\\\caption{\g<2>}\n\
      \\\\end{figure}\n"),                              # images
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

for path, subdirs, files in os.walk("../docs/"):
    #  contents of the converted files
    convertedFiles = {}

    for name in files:
        filePath = os.path.join(path, name)
        fileContents = open(filePath, 'r').read()
        fileOrder = int(search("nav_order: ([0-9]+)", fileContents).group(1))

        # if the file is in the form of \topic\topic.md - the main topic file
        isMainTopic = search("(.+)"+os.sep+"\\\\1\.", filePath) != None

        # the "depth" of the file - how many levels of folders it is in
        fileDepth = filePath[8:].count(os.sep)

        # run the file through the substitution regexes
        for regex in subRegex:
            fileContents = sub(*regex, fileContents, flags=MULTILINE)

        # replace the headings based on the file depth - the further it is in,
        # the more sub will be added in in front of section{...}
        fileContents = sub("^(#+) ([A-Z].+)",\
            lambda x: "\\"\
                + (len(x.group(1)) + fileDepth - 1 - int(isMainTopic)) * "sub"\
                + "section{" + x.group(2)\
                + "}",\
            fileContents, flags=MULTILINE)

        # if it's at depth 0 by default - files like about.md, preface.md...,
        # convertedGroups[fileOrder] will be the file itself
        if fileDepth == 0:
            convertedGroups[fileOrder] = fileContents

        # if it's at depth 0 because it is the main topic,
        # convertedGroups[fileOrder] will be the group of files
        elif fileDepth - int(isMainTopic) == 0:
            convertedGroups[fileOrder] = convertedFiles

        # add the converted file to the fileOrder position
        convertedFiles[fileOrder if not isMainTopic else 0] = fileContents


output = open("output.tex", "w")

# write beginning
output.write(open("beginning", "r").read())

# write the converted articles in their respective order
for k1, v1 in sorted(convertedGroups.items()):
    if type(v1) == str:
        output.write(v1 + "\n")
    else:
        for k2, v2 in sorted(v1.items()):
            output.write(v2 + "\n")

# write ending
output.write(open("ending", "r").read())
