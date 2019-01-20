"""Converts the website into a tex document."""

from regex import sub, search, MULTILINE
from os import path, sep

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


# open the file and write the beginning
latex = open("website.tex", "w")
latex.write(open(path.join("tex-generation-files", "beginning"), "r").read())

for file in open('structure', 'r').read().splitlines():
    # the contents of the file
    content = open(file, 'r').read()

    # if it's a subtopic file (file in a subfolder and not topic/topic.md)
    is_subtopic_file = \
        search(r"(.+)[\\\/]\1\.", file) == None and file.count(sep) == 3

    # special regex for the headings - depends on the docs/ structure
    content = sub(\
        "^(#+) (.+)",\
        lambda x: "\\"\
            + (len(x.group(1)) + is_subtopic_file - 1) * "sub"\
            + "section{" + x.group(2)\
            + "}",\
        content, flags=MULTILINE)

    # run the file through the substitution regexes
    for substitution in substitutions:
        content = sub(*substitution, content, flags=MULTILINE)

    # write the converted content of the file
    latex.write(content)

# write the ending and close the file
latex.write(open(path.join("tex-generation-files", "ending"), "r").read())
latex.close()