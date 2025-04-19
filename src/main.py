import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():

    if len(sys.argv) >1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    docs_dir = "docs"
         
    print("Deleting docs directory...")
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, docs_dir)

    print("Generating page...")
    generate_pages_recursive(dir_path_content,template_path,docs_dir, basepath)
    

if __name__ == "__main__":
	main()