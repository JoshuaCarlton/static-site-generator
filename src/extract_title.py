def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            return title
    raise ValueError("no h1 header found")
