from copy_static_to_public import copy_static_to_public
from generate_page import generate_page


def main():
    copy_static_to_public()
    from_path = "content/index.md"
    dest_path = "public/index.html"
    template_path = "template.html"
    generate_page(from_path, template_path, dest_path)

main()
