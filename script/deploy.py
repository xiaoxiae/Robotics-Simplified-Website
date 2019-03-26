"""Runs all of the scripts and commands necessary to build the website from
scratch and to deploy it via FTP."""

import os

# clean and build website
os.chdir("..")
os.system("bundle exec jekyll clean")
os.system("bundle exec jekyll build")
os.chdir("script")

# generate the sitemap
import sitemap

# generate and convert the latex file to pdf
import tex

# move the PDF file to assets of the website
destination = os.path.join("..", "_site", "assets", "pdf")

if not os.path.exists(destination):
    os.makedirs(destination)
os.rename("website.pdf", os.path.join(destination, "website.pdf"))

# compress all images
import compress

# minify website's source code
import minify

# upload the website
import upload
