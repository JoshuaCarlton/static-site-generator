import os
import shutil

from generate_page import generate_page


def copy_recursive(from_file: str, to_file: str, basepath: str)-> list[str]:
    abs_from_file = os.path.abspath(from_file)
    abs_to_file = os.path.abspath(to_file)
    return copy_from_to(abs_from_file, abs_to_file, basepath)

def copy_from_to(from_file: str, to_file: str, basepath: str)-> list[str]:
    copyed: list[str] = []
    contents = os.listdir(from_file)
    abs_template = os.path.abspath("template.html")
    for content in contents:
        abs_content = os.path.join(from_file, content)
        abs_destination = os.path.join(to_file, content)
        if os.path.isfile(abs_content):
            if abs_content.endswith(".md"):
                generate_page(abs_content, abs_template, abs_destination.replace(".md", ".html"), basepath)
            else:
                shutil.copy(abs_content, abs_destination)
        else:
            os.mkdir(abs_destination)
            copyed.extend(copy_from_to(abs_content, abs_destination, basepath))
        copyed.append(abs_content)
    return copyed
