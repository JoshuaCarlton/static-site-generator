import unittest

from extract import extract_markdown_images, extract_markdown_links


class TestsExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links_image(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_images_link(self):
        matches = extract_markdown_images(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_malformated_link(self):
        matches = extract_markdown_links(
            "This is text with a [link] (https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_extra_brackets(self):
        matches = extract_markdown_links(
            "This is text with a [[[link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_multiple_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)  it also has ![wonky image](atsomeplace.com)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("wonky image", "atsomeplace.com")], matches)

    def test_extract_markdown_multiple_links(self):
        matches = extract_markdown_images(
            "This is text with an ![link](https://i.imgur.com/zjjcJKZ.png)  it also has ![wonky link](atsomeplace.com)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png"), ("wonky link", "atsomeplace.com")], matches)

    def test_extract_markdown_link_and_image(self):
        text = "This is text with a [link](https://i.imgur.com/zjjcJKZ.png)  it also has ![wonky image](atsomeplace.com)"
        images = extract_markdown_images(text)
        links = extract_markdown_links(text)
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], links)
        self.assertListEqual([("wonky image", "atsomeplace.com")], images)
