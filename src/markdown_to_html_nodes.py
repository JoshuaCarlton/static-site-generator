import re

from htmlnode import HTMLNode, ParentNode
from markdown_block_type import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    div_children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        div_children.append(create_parent_node(block, block_type))
    div = ParentNode("div", div_children)
    return div


def create_parent_node(block: str, block_type: BlockType) -> ParentNode:
    match block_type:
        case BlockType.PARAGRAPH:
            block_children = block_to_html_nodes(block.replace("\n", " "))
            return ParentNode("p", block_children)
        case BlockType.HEADING:
            heading = re.findall(r"(?<!.)#{1,6} ", block)[0]
            pounds = len(heading) - 1
            block = block.replace(heading, "")
            block_children = block_to_html_nodes(block)
            return ParentNode(f"h{pounds}", block_children)
        case BlockType.QUOTE:
            old_lines = block.split("\n")
            new_lines = []
            for old_line in old_lines:
                if len(old_line) == 1:
                    new_line = ""
                elif old_line[1] == " ":
                    new_line = old_line[2:]
                else:
                    new_line = old_line[1:]
                new_lines.append(new_line)
            new_block = "\n".join(new_lines)
            block_children = block_to_html_nodes(new_block)
            return ParentNode("blockquote", block_children)
        case BlockType.UNORDERED_LIST:
            old_lines = block.split("\n")
            line_items = []
            for old_line in old_lines:
                new_line = old_line[2:]
                line_item_children = block_to_html_nodes(new_line)
                line_items.append(ParentNode("li", line_item_children))
            return ParentNode("ul", line_items)
        case BlockType.ORDERED_LIST:
            old_lines = block.split("\n")
            line_items = []
            for old_line in old_lines:
                number = re.findall(r"(?<!.)\d*\. ", old_line)[0]
                new_line = old_line[len(number) :]
                line_item_children = block_to_html_nodes(new_line)
                line_items.append(ParentNode("li", line_item_children))
            return ParentNode("ol", line_items)
        case BlockType.CODE:
            block = block[4:-3]
            code_text = TextNode(block, TextType.CODE)
            code = text_node_to_html_node(code_text)
            return ParentNode("pre", [code])
    raise ValueError("invalid block type")


def block_to_html_nodes(block: str) -> list[HTMLNode]:
    block_children = []
    text_nodes = text_to_textnodes(block)
    for text_node in text_nodes:
        block_children.append(text_node_to_html_node(text_node))
    return block_children
