import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_tag(self):
        node = HTMLNode(tag="taggy")

        self.assertEqual(node.tag, "taggy")

    def test_props(self):
        node = HTMLNode(props = {
            "href": "https://www.google.com",
            "target": "_blank",
        })

        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_noprops(self):
        node = HTMLNode(tag="taggy")

        self.assertEqual(node.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_none(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)  # pyright: ignore[reportArgumentType]
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parrent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parrent_node_no_children(self):
        node = ParentNode("p", [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parrent_node_none_children(self):
        node = ParentNode("p", None)  # pyright: ignore[reportArgumentType]
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parrent_node_no_tag(self):
        node = ParentNode(
            "",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        with self.assertRaises(ValueError):
            node.to_html()
