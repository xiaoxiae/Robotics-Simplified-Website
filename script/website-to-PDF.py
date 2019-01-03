from re import sub, match, search, MULTILINE
import os

# regular expressions and their substitution results
subRegex = [
    ("---\n(.+\n)+---", ""),                            # remove config
    ("^---\n", ""),                                     # remove linebreaks
    ("\\\\(sub)*section{Visualization}\n(.*\n)+^\\\\",\
     "\\\\"),                                           # remove visualizations
    ("(```python\n){% +include +(.+?) +%}(\n```)",\
        lambda x: x.group(1) + \
        open(".."+os.sep+"_includes"+os.sep+x.group(2), "r").read() + \
        x.group(3)),                                    # insert code snippet
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
        fPath = os.path.join(path, name)
        fContent = open(fPath, 'r').read()
        fileOrder = int(search("nav_order: ([0-9]+)", fContent).group(1))

        # if the file is in the form of \topic\topic.md - the main topic file
        isMainTopic = search("(.+)"+os.sep+"\\\\1\.", filePath) != None

        # the "depth" of the file - how many levels of folders it is in
        fDepth = fPath[8:].count(os.sep)

        # replace the headings based on the file depth - the further it is in,
        # the more sub will be added in in front of section{...}
        fContent = sub("^(#+) (.+)",\
            lambda x: "\\"\
                + (len(x.group(1)) + fDepth - 1 - int(isMainTopic)) * "sub"\
                + "section{" + x.group(2)\
                + "}",\
            fContent, flags=MULTILINE)

        # run the file through the substitution regexes
        for regex in subRegex:
            fContent = sub(*regex, fContent, flags=MULTILINE)

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
latexOut = open("latexOut.tex", "w")

# write beginning
latexOut.write(open("tex-generation-files" + os.sep + "beginning", "r").read())

# write the converted articles in their respective order
for k1, v1 in sorted(convertedGroups.items()):
    if type(v1[0]) == str:
        latexOut.write(v1[0] + "\n")
    else:
        for k2, v2 in sorted(v1.items()):
            latexOut.write(v2[0] + "\n")

# write ending
latexOut.write(open("tex-generation-files" + os.sep + "ending", "r").read())
