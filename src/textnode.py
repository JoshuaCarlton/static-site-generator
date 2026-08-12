from enum import Enum

from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, content: str, text_type: TextType, url: str | None = None):
        self.text = content
        self.text_type = text_type
        self.url = url

    def __eq__(self, value: object, /) -> bool:
        if isinstance(value, TextNode):
            return bool(self.text == value.text
                and self.text_type == value.text_type
                and self.url == value.url)
        return False

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type is None:
        raise Exception("not a TextType")  # noqa: TRY002
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            if text_node.url == None:
                raise ValueError("no url")
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            if text_node.url == None:
                raise ValueError("no url")
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
