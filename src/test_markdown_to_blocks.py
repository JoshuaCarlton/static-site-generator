import unittest

from markdown_to_blocks import markdown_to_blocks


class TestMarkDownToBlcoks(unittest.TestCase):
    def test_one_liners(self):
        text = """
there once was a ship who put to sea

and the name of the ship was a billy o tea

the winds blew up her bow dipped down and away the billy did blow



        """
        actual = markdown_to_blocks(text)
        expected = [
            "there once was a ship who put to sea",
            "and the name of the ship was a billy o tea",
            "the winds blew up her bow dipped down and away the billy did blow",
        ]
        self.assertEqual(actual, expected)

    def template(self):
        text = """
        """
        actual = markdown_to_blocks(text)
        expected = [
        ]
        self.assertEqual(actual, expected)

    def test_paragraphs(self):
        text = """
line1
line2
line3

new paragraph
yodelayhoo

new line

        """
        actual = markdown_to_blocks(text)
        expected = [
            """line1\nline2\nline3""",
            """new paragraph\nyodelayhoo""",
            "new line"
        ]
        self.assertEqual(actual, expected)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line





- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
