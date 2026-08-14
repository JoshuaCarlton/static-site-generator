import os
import shutil


def copy_static_to_public()-> list[str]:
    abs_static = os.path.abspath("static")
    abs_public = os.path.abspath("public")
    if os.path.exists(abs_public):
        shutil.rmtree(abs_public)
    os.mkdir(abs_public)
    return copy_from_to(abs_static, abs_public)

def copy_from_to(from_file: str, to_file: str)-> list[str]:
    copyed: list[str] = []
    contents = os.listdir(from_file)
    for content in contents:
        abs_content = os.path.join(from_file, content)
        abs_destination = os.path.join(to_file, content)
        if os.path.isfile(abs_content):
            shutil.copy(abs_content, abs_destination)
        else:
            os.mkdir(abs_destination)
            copyed.extend(copy_from_to(abs_content, abs_destination))
        copyed.append(abs_content)
    return copyed
