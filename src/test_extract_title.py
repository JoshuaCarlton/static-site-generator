import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_title(self):
        md = """
# here is the title

here is some paragraphs and such
why? idk."""
        actual = extract_title(md)
        expected = "here is the title"
        self.assertEqual(actual, expected)

    def test_two_titles(self):
        md = """
# here is the title
# here is the other title

here is some paragraphs and such
why? idk."""
        actual = extract_title(md)
        expected = "here is the title"
        self.assertEqual(actual, expected)

    def test_h2_title(self):
        md = """
## here is the title
# but that one is too big, use this instead

here is some paragraphs and such
why? idk."""
        actual = extract_title(md)
        expected = "but that one is too big, use this instead"
        self.assertEqual(actual, expected)
