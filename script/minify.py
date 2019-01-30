"""Minifies website source files."""

from os import path, walk
from css_html_js_minify import minify

allowed_extensions = ("css", "html")

# sizes for each extension before and after
size_before = [0] * len(allowed_extensions)
size_after = [0] * len(allowed_extensions)

# recursively find website source files
for root, subdirs, files in walk(path.join("..", "_site")):
    for file in files:
        if file.endswith(allowed_extensions):
            file_path = path.join(root, file)
            file_extension = file[file.index(".") + 1:]

            # add size before minifying
            size_before[allowed_extensions.index(file_extension)] += \
                path.getsize(file_path)

            # minify
            minify.process_multiple_files(file_path, overwrite = True)

            # add size after minifying
            size_after[allowed_extensions.index(file_extension)] += \
                path.getsize(file_path)

# print minify stats
for i in range(len(allowed_extensions)):
    print(allowed_extensions[i].upper() + " compression rate: "\
          + str(round(size_after[i] / size_before[i] * 100, 2)) + "%,"\
          + "saved " + str(round((size_before[i] - size_after[i]) / 1024, 2))\
          + " KB")
