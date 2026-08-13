def markdown_to_blocks(markdown: str)  -> list[str]:
    unstripped = markdown.split("\n\n")
    blocks = []
    for block in unstripped:
        if block.strip() != "":
            blocks.append(block.strip())
    return blocks
