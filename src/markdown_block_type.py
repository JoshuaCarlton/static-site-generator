import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown: str) -> BlockType:
    heading = re.findall(r"(?<!.)#{1,6} ", markdown)
    if heading:
        return BlockType.HEADING
    code = re.findall(r"(?<!.)```\n(?s:.)*```(?!.)", markdown)
    if code:
        return BlockType.CODE
    lines = markdown.split("\n")
    quote = True
    for line in lines:
        if not re.findall(r"(?<!.)>.", line):
            quote = False
            break
    if quote:
        return BlockType.QUOTE
    unordered = True
    for line in lines:
        if not re.findall("(?<!.)- ", line):
            unordered = False
            break
    if unordered:
        return BlockType.UNORDERED_LIST
    ordered = True
    for i in range(len(lines)):
        line = lines[i]
        if line[0] != str(i + 1) or line[1] != ".":
            ordered = False
            break
    if ordered:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
