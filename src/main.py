from textnode import TextNode, TextType


def main():
    dummy = TextNode("dummy", TextType.LINK, "https/dummy.com")
    print(dummy)

main()
