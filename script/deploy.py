"""Runs all of the scripts and commands necessary to build the website from
scratch and to deploy it with FTP."""
import os
import subprocess

# build website
os.chdir("..")
os.system("jekyll build")
os.chdir("script")

# generate sitemap and latex files
import generate

# convert latex file to pdf
subprocess.call("pdflatex -interaction=nonstopmode website.tex")

# move the PDF file to assets of the website
destination = os.path.join("..", "_site", "assets", "pdf")

if not os.path.exists(destination):
    os.makedirs(destination)
os.rename("website.pdf", os.path.join(destination, "website.pdf"))

# clean-up unnecessary tex files
for f in os.listdir('.'):
    if os.path.isfile(f) and "website" in f:
        os.remove(f)

# upload the website
import upload