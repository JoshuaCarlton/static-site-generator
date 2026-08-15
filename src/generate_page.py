import os

from extract_title import extract_title
from markdown_to_html_nodes import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        content = f.read()
    with open(template_path) as t:
        template = t.read()
    title = extract_title(content)
    template = template.replace("{{ Title }}", title)
    htmlnode = markdown_to_html_node(content)
    html = htmlnode.to_html()
    template = template.replace("{{ Content }}", html)
    dir_path = "/".join(dest_path.split("/")[:-1])
    os.makedirs(dir_path, exist_ok=True)
    with open(dest_path, "w") as d:
        d.write(template)
