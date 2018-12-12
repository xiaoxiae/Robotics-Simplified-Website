from ftplib import FTP
import os
import getpass

def remove_content():
    """Recursively removes all content that isn't on the permanent list."""
    # for all subdirectories of the current directory
    for content in ftp.nlst():
        # if the content isn't permanent
        if content not in permanent_content:
            if "." in content:
                # if it's a file, delete it immediately
                print("DELETED FILE: "+ftp.pwd()+content)
                ftp.delete(content)
            else:
                # move down to the directory and call remove_content
                ftp.cwd(content)
                remove_content()

                # move up a directory and delete the folder
                ftp.cwd("..")
                ftp.rmd(content)
                print("DELETED FOLDER: "+ftp.pwd()+content)


def add_content():
    "Recursively adds the content from the _site folder to the website."
    # move to the _site
    os.chdir("_site")

    # get all directories
    directories = []
    for directory in [dir[0] for dir in os.walk(".")]:
        if directory[2:] != "":
            directories.append(directory[2:].replace("\\", "/"))

    # upload all directories
    for directory in sorted(directories):
        ftp.mkd(directory)
        print("CREATED DIRECTORY: "+directory)

    # get all files
    files = [os.path.join(root, name)[2:].replace("\\", "/")
            for root, dirs, files in os.walk(".")
            for name in files]

    # upload all files
    for file in files:
        ftp.storbinary('STOR '+file, open(file, "rb"))
        print("CREATED FILE: "+file)


permanent_content = ["info.php", "subdom", "domains", ".htaccess"]

# connect to the server
with FTP("89.221.213.4", input("Login: "), getpass.getpass("Password: ")) as ftp:
    print("Connected!")
    print(ftp.cwd('www'))

    # remove all content that isn't permanent
    remove_content()

    # add all content from _site folder
    add_content()

    # disconnect from the server
    print(ftp.quit())
