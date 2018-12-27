from re import sub, match, search, MULTILINE
import os

# regular expressions and their substitution results
subRegex = [
    ("---\n(.+\n)+---", ""),                            # remove config
    ("```python(\n(.*\n)+?)```",            # code highlights with lstlisting
     "\\\\begin{lstlisting}\g<1>\\\\end{lstlisting}"),
    ("\*\*(.+?)\*\*", "\\\\textbf{\g<1>}"),             # bold text
    ("\*(.+?)\*", "\\\\textit{\g<1>}"),                 # italics
    ("\[(.+?)\]\((.+?)\)", "\\\\href{\g<2>}{\g<1>}"),   # href
    ("(.+?)\$(\$.*?\$)\$(.+?)", "\g<1>\g<2>\g<3>"),     # $$.$$ to $.$
    ("`([^`\n]+?)`","\\\\texttt{\g<1>}"),               # `` md highlights
    ("ttt{([^}]+?)_([^{]+?)}","ttt{\g<1>\_\g<2>}"),     # escape _ in texttt
    ("^(- .+\n)+", "\\\\begin{itemize}\n\g<0>\\\\end{itemize}"),    # itemize
    ("(^- (.+)\n)+?", "\\\\item \g<2>\n")               # - to \item
]

# read through all of the files
for path, subdirs, files in os.walk("../docs/"):
    for name in files:
        fileName = os.path.join(path, name)
        fileContents = open(fileName, 'r').read()
        fileOrder = search("nav_order: ([0-9]+)", fileContents).group(1)

        # run the file through the substitution regexes
        for regex in subRegex:
            fileContents = sub(*regex, fileContents, flags=MULTILINE)


output = open("output.tex", "w")

# we have to add \n characters to lines manually, because writelines() doesn't
nl = lambda x:x+"\n"

# write the beginning
beginning = list(map(nl, open("beginning", "r").read().splitlines()))
output.writelines(beginning)

# write the end
ending = list(map(nl, open("ending", "r").read().splitlines()))
output.writelines(ending)
