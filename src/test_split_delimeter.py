import unittest

from extract import split_nodes_delimiter
from textnode import TextNode, TextType


class TestsSplitDelimeter(unittest.TestCase):
    def test_split_bold(self):
        node = TextNode("this node has **bolded text** in it.", TextType.TEXT)
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("this node has ", TextType.TEXT),
            TextNode("bolded text", TextType.BOLD),
            TextNode(" in it.", TextType.TEXT),
        ]
        self.assertEqual(actual, expected)

    def test_split_end(self):
        node = TextNode("this node has **bolded text**", TextType.TEXT)
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("this node has ", TextType.TEXT),
            TextNode("bolded text", TextType.BOLD),
        ]
        self.assertEqual(actual, expected)

    def test_split_multi(self):
        node = TextNode("this node has **multiple sections** with **bolded text** inside it", TextType.TEXT)
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("this node has ", TextType.TEXT),
            TextNode("multiple sections", TextType.BOLD),
            TextNode(" with ", TextType.TEXT),
            TextNode("bolded text", TextType.BOLD),
            TextNode(" inside it", TextType.TEXT)
        ]
        self.assertEqual(actual, expected)

    def test_split_incomplete(self):
        node = TextNode("this **bold section has no closing delimeter", TextType.TEXT)
        with self.assertRaises(Exception):  # noqa: B017
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_split_multiple_nodes(self):
        node1 = TextNode("this node has **bolded text** in it.", TextType.TEXT)
        node2 = TextNode("this node has **fancy** in it.", TextType.TEXT)
        node3 = TextNode("this node has **poodles in swimsuits** in it.", TextType.TEXT)
        actual = split_nodes_delimiter([node1, node2, node3], "**", TextType.BOLD)
        expected = [
            TextNode("this node has ", TextType.TEXT),
            TextNode("bolded text", TextType.BOLD),
            TextNode(" in it.", TextType.TEXT),
            TextNode("this node has ", TextType.TEXT),
            TextNode("fancy", TextType.BOLD),
            TextNode(" in it.", TextType.TEXT),
            TextNode("this node has ", TextType.TEXT),
            TextNode("poodles in swimsuits", TextType.BOLD),
            TextNode(" in it.", TextType.TEXT),
        ]
        self.assertEqual(actual, expected)

    def test_no_delimeter(self):
        node = TextNode("there is no delimeter in ba sing se", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "", TextType.BOLD)

    def test_split_code(self):
        node = TextNode("this node has ~code~ in it.", TextType.BOLD)
        actual = split_nodes_delimiter([node], "~", TextType.CODE)
        expected = [
            TextNode("this node has ", TextType.BOLD),
            TextNode("code", TextType.CODE),
            TextNode(" in it.", TextType.BOLD),
        ]
        self.assertEqual(actual, expected)
