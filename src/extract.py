import re

from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    if delimiter == "":
        raise ValueError("no delimeter set")
    new_nodes = []
    for old_node in old_nodes:
        parts = old_node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception("opening delimeter found without closing delimiter")  # noqa: TRY002
        inside_delimeter = False
        for part in parts:
            if inside_delimeter == False:
                if part != "":
                    new_nodes.append(TextNode(part, old_node.text_type, old_node.url))
                inside_delimeter = True
            else:
                if part != "":
                    new_nodes.append(TextNode(part, text_type))
                    inside_delimeter = False
    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[([^\[\]\n]*)\]\(([^\(\)\n]*)\)", text)

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"(?<!!)\[([^\[\]\n]*)\]\(([^\(\)\n]*)\)", text)

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        text = old_node.text
        images = extract_markdown_images(text)
        for image in images:
            begining, text = text.split(f"![{image[0]}]({image[1]})", 1)
            if begining != "":
                new_nodes.append(TextNode(begining, old_node.text_type))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
        if text != "":
            new_nodes.append(TextNode(text, old_node.text_type, old_node.url))
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        text = old_node.text
        links = extract_markdown_links(text)
        for link in links:
            begining, text = text.split(f"[{link[0]}]({link[1]})", 1)
            if begining != "":
                new_nodes.append(TextNode(begining, old_node.text_type))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
        if text != "":
            new_nodes.append(TextNode(text, old_node.text_type, old_node.url))
    return new_nodes
