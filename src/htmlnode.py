class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props == None:
            return ""
        props = ""
        for item in self.props.items():
            key, value = item
            props += f' {key}="{value}"'
        return props

    def __repr__(self) -> str:
        return f"tag={self.tag} value={self.value} node has {len(self.children) if self.children is not None else "no"} children props={self.props_to_html()}"

class LeafNode(HTMLNode):
    def __init__(
        self, tag: str | None,
        value: str,
        props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.tag == "img":
            assert self.props is not None
            return f'<img src="{self.props["src"]}" alt="{self.props["alt"]}" />'
        if self.value == None:
            raise ValueError("value not set")
        if self.tag == "a":
            assert self.props is not None
            return f'<a href="{self.props["href"]}">{self.value}</a>'
        if self.tag == None:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"tag={self.tag} value={self.value} props={self.props_to_html()}"

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list["HTMLNode"], props: dict[str, str] | None = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("no tag set")
        if self.children == None or len(self.children) == 0:
            raise ValueError("no children")
        html = f"<{self.tag}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html
