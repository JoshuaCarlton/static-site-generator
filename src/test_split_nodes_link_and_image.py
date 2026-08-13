import unittest

from extract import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


class TestsSplitImageLink(unittest.TestCase):
    def test_split_image(self):
        node = TextNode("this node has an ![image](https.somewhere.com) in it.", TextType.TEXT)
        actual = split_nodes_image([node])
        expected = [
            TextNode("this node has an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https.somewhere.com"),
            TextNode(" in it.", TextType.TEXT),
        ]
        self.assertEqual(actual, expected)

    def test_split_duplicate_image(self):
        node = TextNode("this node has two images ![image](https.somewhere.com) ![image](https.somewhere.com) in it.", TextType.TEXT)
        actual = split_nodes_image([node])
        expected = [
            TextNode("this node has two images ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https.somewhere.com"),
            TextNode(" ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https.somewhere.com"),
            TextNode(" in it.", TextType.TEXT),

        ]
        self.assertEqual(actual, expected)

    def test_split_link(self):
        node = TextNode("this node has a [link](https.somewhere.com) in it.", TextType.TEXT)
        actual = split_nodes_link([node])
        expected = [
            TextNode("this node has a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https.somewhere.com"),
            TextNode(" in it.", TextType.TEXT),
        ]
        self.assertEqual(actual, expected)

    def test_split_duplicate_link(self):
        node = TextNode("this node has two links [link](https.somewhere.com) [link](https.somewhere.com) in it.", TextType.TEXT)
        actual = split_nodes_link([node])
        expected = [
            TextNode("this node has two links ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https.somewhere.com"),
            TextNode(" ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https.somewhere.com"),
            TextNode(" in it.", TextType.TEXT),
        ]
        self.assertEqual(actual, expected)

    def test_split_multiple_link(self):
        node = TextNode("this node has two links [linky](https.somewhere.com) [link](https.somewherebarnaby.com) in it.", TextType.TEXT)
        actual = split_nodes_link([node])
        expected = [
            TextNode("this node has two links ", TextType.TEXT),
            TextNode("linky", TextType.LINK, "https.somewhere.com"),
            TextNode(" ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https.somewherebarnaby.com"),
            TextNode(" in it.", TextType.TEXT),
        ]
        self.assertEqual(actual, expected)

    def test_split_link_with_image(self):
        node = TextNode("this node has two links ![imagey](https.somewhere.com) [link](https.somewherebarnaby.com) in it.", TextType.TEXT)
        actual = split_nodes_link([node])
        expected = [
            TextNode("this node has two links ![imagey](https.somewhere.com) ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https.somewherebarnaby.com"),
            TextNode(" in it.", TextType.TEXT),
        ]
        self.assertEqual(actual, expected)

    def test_split_link_and_image(self):
        node = TextNode("this node has two links ![image](https.somewhere.com) [link](https.somewherebarnaby.com) in it.", TextType.TEXT)
        actual = split_nodes_image(split_nodes_link([node]))
        expected = [
            TextNode("this node has two links ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https.somewhere.com"),
            TextNode(" ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https.somewherebarnaby.com"),
            TextNode(" in it.", TextType.TEXT),
        ]
        self.assertEqual(actual, expected)


    def test_split_multiple_links_and_images(self):
        node = TextNode("""this string has lots of things in it first it has
            a picture of a dog ![dog](dogpics.com) isnt he cute?
            We also have a link to a website about [cats](catsrus.edu) very informative
            we also have [crazy tom](tomsblog.com)![pic of tom](wierdguys.com)""", TextType.TEXT)
        actual = split_nodes_image(split_nodes_link([node]))
        expected = [
            TextNode("""this string has lots of things in it first it has
            a picture of a dog """, TextType.TEXT),
            TextNode("dog", TextType.IMAGE, "dogpics.com"),
            TextNode(""" isnt he cute?
            We also have a link to a website about """, TextType.TEXT),
            TextNode("cats", TextType.LINK, "catsrus.edu"),
            TextNode(""" very informative
            we also have """, TextType.TEXT),
            TextNode("crazy tom", TextType.LINK, "tomsblog.com"),
            TextNode("pic of tom", TextType.IMAGE, "wierdguys.com"),
        ]
        self.assertEqual(actual, expected)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
