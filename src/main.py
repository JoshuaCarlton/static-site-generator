from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main():
    dummy = TextNode("dummy", TextType.LINK, "https/dummy.com")
    print(dummy)
    htmlnode = HTMLNode(tag = "taggy", value = "42", props = {
        "href": "https://www.google.com",
        "target": "_blank",
    })
    print(htmlnode)


main()
