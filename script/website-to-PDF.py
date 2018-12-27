from re import sub, match, search
import os


# read through all of the files
for path, subdirs, files in os.walk("../docs/"):
    for name in files:
        fileName = os.path.join(path, name)
        fileContents = open(fileName, 'r').read()
        fileOrder = search("nav_order: ([0-9]+)", fileContents).group(1)

        # convert the file to a latex file
        fileContents =  sub("---\n(.+\n)+---", "",\
                        sub("```python(\n(.*\n)+?)```",\
                            "\\\\begin{lstlisting}\g<1>\\\\end{lstlisting}",\
                        sub("\*(.+?)\*", "\\\\textit{\g<1>}",
                        sub("\*\*(.+?)\*\*", "\\\\textbf{\g<1>}",
                        sub("\[(.+?)\]\((.+?)\)", "\\\\href{\g<2>}{\g<1>}",\
                        sub("(.+?)\$(\$.*?\$)\$(.+?)", "\g<1>\g<2>\g<3>",\
                        sub("`([^`\n]+?)`","\\\\texttt{\g<1>}",\
                            fileContents)))))))

        convertedContent.append(fileContents)


output = open("output.tex", "w")

# we have to add \n characters to lines manually, because writelines() doesn't
nl = lambda x:x+"\n"

# write the beginning
beginning = list(map(nl, open("beginning", "r").read().splitlines()))
output.writelines(beginning)

# write the end
ending = list(map(nl, open("ending", "r").read().splitlines()))
output.writelines(ending)
