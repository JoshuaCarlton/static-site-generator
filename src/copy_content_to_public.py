import os
import shutil

from generate_page import generate_page


def copy_content_to_public()-> list[str]:
    abs_content = os.path.abspath("content")
    abs_public = os.path.abspath("public")
    return copy_from_to(abs_content, abs_public)

def copy_from_to(from_file: str, to_file: str)-> list[str]:
    copyed: list[str] = []
    contents = os.listdir(from_file)
    abs_template = os.path.abspath("template.html")
    for content in contents:
        abs_content = os.path.join(from_file, content)
        abs_destination = os.path.join(to_file, content)
        if os.path.isfile(abs_content):
            if abs_content.endswith(".md"):
                generate_page(abs_content, abs_template, abs_destination.replace(".md", ".html"))
            else:
                shutil.copy(abs_content, abs_destination)
        else:
            os.mkdir(abs_destination)
            copyed.extend(copy_from_to(abs_content, abs_destination))
        copyed.append(abs_content)
    return copyed
