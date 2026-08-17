import os
import shutil
import sys

from copy_recursive import copy_recursive


def main():
    dest_file = "docs"
    abs_to_file = os.path.abspath(dest_file)
    if os.path.exists(abs_to_file):
        shutil.rmtree(abs_to_file)
    os.mkdir(abs_to_file)
    argv = sys.argv
    basepath = "/"
    if len(argv) > 1:
        basepath = argv[1]
    copy_recursive("static", dest_file, basepath)
    copy_recursive("content", dest_file, basepath)


main()
