from extract import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


def text_to_textnodes(text: str) -> list[TextNode]:
    node = TextNode(text, TextType.TEXT)
    imaged = split_nodes_image([node])
    linked = split_nodes_link(imaged)
    bolded = split_nodes_delimiter(linked, "**", TextType.BOLD)
    italiced = split_nodes_delimiter(bolded, "_", TextType.ITALIC)
    coded = split_nodes_delimiter(italiced, "`", TextType.CODE)
    return coded
