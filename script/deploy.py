"""Runs all of the scripts and commands necessary to build the website from
scratch and to deploy it via FTP."""

import os
import subprocess

# clean and build website
os.chdir("..")
os.system("jekyll clean")
os.system("jekyll build")
os.chdir("script")

# generate necessary files
import generate_docs_structure
import generate_sitemap
import generate_tex_file

# convert latex file to pdf (twice, so contents are generated properly)
for _i in range(2):
    subprocess.call(r"pdflatex -interaction=nonstopmode website.tex", shell=True)

# move the PDF file to assets of the website
destination = os.path.join("..", "_site", "assets", "pdf")

if not os.path.exists(destination):
    os.makedirs(destination)
os.rename("website.pdf", os.path.join(destination, "website.pdf"))

# clean-up unnecessary tex files
for f in os.listdir('.'):
    if os.path.isfile(f) and not f.endswith("py"):
        os.remove(f)

# upload the website
import upload
