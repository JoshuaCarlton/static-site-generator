import unittest

from markdown_to_html_nodes import markdown_to_html_node


class TestMarkdownHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_link(self):
        md = """
here is a paragraph with a [link](https/linky.com) in it
here is another one [second](https/lonks.com)
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>here is a paragraph with a <a href="https/linky.com">link</a> in it here is another one <a href="https/lonks.com">second</a></p></div>'
        )

    def test_image(self):
        md = """
here is a paragraph with a ![picture](https/linky.com) in it
here is another one ![second](https/lonks.com)
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>here is a paragraph with a <img src="https/linky.com" alt="picture" /> in it here is another one <img src="https/lonks.com" alt="second" /></p></div>'
        )

    def test_quote_with_image(self):
        md = """
> here is a paragraph with a ![picture](https/linky.com) in it
> here is another one ![second](https/lonks.com)
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><blockquote>here is a paragraph with a <img src="https/linky.com" alt="picture" /> in it\nhere is another one <img src="https/lonks.com" alt="second" /></blockquote></div>'
        )

    def test_unordered_list(self):
        md = """
- this is an unordered list
- it might have stuff in it like **bold** text
- or some _italics_
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ul><li>this is an unordered list</li><li>it might have stuff in it like <b>bold</b> text</li><li>or some <i>italics</i></li></ul></div>'
        )

    def test_ordered_list(self):
        md = """
1. this is an ordered list
2. it might have stuff in it like **bold** text
3. or some _italics_
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ol><li>this is an ordered list</li><li>it might have stuff in it like <b>bold</b> text</li><li>or some <i>italics</i></li></ol></div>'
        )

    def test_ordered_list_long(self):
        md = """
1. a
2. a
3. a
4. a
5. a
6. a
7. a
8. a
9. a
10. a
11. a
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ol><li>a</li><li>a</li><li>a</li><li>a</li><li>a</li><li>a</li><li>a</li><li>a</li><li>a</li><li>a</li><li>a</li></ol></div>'
        )

    def test_heading(self):
        md = """
#### this is a heading part of it could be **bold** too

here is a paragraph after that
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h4>this is a heading part of it could be <b>bold</b> too</h4><p>here is a paragraph after that</p></div>'
        )

    def test_everything_at_once(self):
        md = """
### first is the **heading** of course

then the paragraph where we talk about things
and also _crazy_ things
we can show a picture of crazy tom ![crazy tom](https/toms_crazy_things.com)
and we can show a link to [wikipedia](wikipedia.com)
we might want to show off some `code` too

- now we were really missing some lists
- so lets add those

1. cant forget ordered lists
2. it wouldnt be complete without one

> as einstien once said
> "I never said any of that"

```
here is some code too```
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h3>first is the <b>heading</b> of course</h3><p>then the paragraph where we talk about things and also <i>crazy</i> things we can show a picture of crazy tom <img src="https/toms_crazy_things.com" alt="crazy tom" /> and we can show a link to <a href="wikipedia.com">wikipedia</a> we might want to show off some <code>code</code> too</p><ul><li>now we were really missing some lists</li><li>so lets add those</li></ul><ol><li>cant forget ordered lists</li><li>it wouldnt be complete without one</li></ol><blockquote>as einstien once said\n"I never said any of that"</blockquote><pre><code>here is some code too</code></pre></div>'
        )
