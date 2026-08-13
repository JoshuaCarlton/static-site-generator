import unittest

from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType


class TestsTextToTextnodes(unittest.TestCase):
    def test_image(self):
        actual = text_to_textnodes("this node has an ![image](https.somewhere.com) in it.")
        expected = [
            TextNode("this node has an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https.somewhere.com"),
            TextNode(" in it.", TextType.TEXT),
        ]
        self.assertEqual(actual, expected)

    def test_lanes_example(self):
        actual = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(actual, expected)

    def test_no_text(self):
        actual = text_to_textnodes("**Bold**_Italic_`Code Block`![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)[link](https://boot.dev)")
        expected = [
            TextNode("Bold", TextType.BOLD),
            TextNode("Italic", TextType.ITALIC),
            TextNode("Code Block", TextType.CODE),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(actual, expected)

    def test_no_text_shuffle(self):
        actual = text_to_textnodes("![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)`Code Block`**Bold**[link](https://boot.dev)_Italic_")
        expected = [
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("Code Block", TextType.CODE),
            TextNode("Bold", TextType.BOLD),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode("Italic", TextType.ITALIC),
        ]
        self.assertEqual(actual, expected)

    def test_no_text_doubled(self):
        actual = text_to_textnodes("**Bold**_Italic_`Code Block`![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)[link](https://boot.dev)**Bold**_Italic_`Code Block`![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)[link](https://boot.dev)")
        expected = [
            TextNode("Bold", TextType.BOLD),
            TextNode("Italic", TextType.ITALIC),
            TextNode("Code Block", TextType.CODE),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode("Bold", TextType.BOLD),
            TextNode("Italic", TextType.ITALIC),
            TextNode("Code Block", TextType.CODE),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(actual, expected)

    def test_bad_characters(self):
        actual = text_to_textnodes("this node ![]has ()an !![image](https.somewhere.com))) in ((([[[it.")
        expected = [
            TextNode("this node ![]has ()an !", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https.somewhere.com"),
            TextNode(")) in ((([[[it.", TextType.TEXT),
        ]
        self.assertEqual(actual, expected)
