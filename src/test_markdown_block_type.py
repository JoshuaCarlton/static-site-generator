import unittest

from markdown_block_type import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks


class TestMarkDownToBlcoks(unittest.TestCase):
    def test_paragraph(self):
        text = """
this is just a noraml paragrahp
nothing special
just some stuff
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.PARAGRAPH
        self.assertEqual(actual, expected)

    def test_heading(self):
        text = """
### header this is a header
and if i keep typing it should still be a header
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.HEADING
        self.assertEqual(actual, expected)

    def test_heading_7pound(self):
        text = """
####### header this is a header
and if i keep typing it should still be a header
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.PARAGRAPH
        self.assertEqual(actual, expected)

    def test_heading_extra(self):
        text = """
y##### header this is a header
and if i keep typing it should still be a header
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.PARAGRAPH
        self.assertEqual(actual, expected)

    def test_code(self):
        text = """```
this is a code block
coding coding coding
```
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.CODE
        self.assertEqual(actual, expected)

    def test_code_no_newline(self):
        text = """```this is a code block coding coding coding```
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.PARAGRAPH
        self.assertEqual(actual, expected)

    def test_code_no_endline(self):
        text = """```
this is a code block
coding coding coding```"""
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.CODE
        self.assertEqual(actual, expected)

    def test_code_extra(self):
        text = """g```
this is a code block
coding coding coding
```
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.PARAGRAPH
        self.assertEqual(actual, expected)

    def test_quote(self):
        text = """
> this is a quote.
> who am i quoting?
> who cares you just need to know this is a quote.
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.QUOTE
        self.assertEqual(actual, expected)

    def test_quote_partial(self):
        text = """
> this is a quote.
> who am i quoting?
who cares you just need to know this is a quote.
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.PARAGRAPH
        self.assertEqual(actual, expected)

    def test_quote_bad_start(self):
        text = """
//> this is a quote.
> who am i quoting?
> who cares you just need to know this is a quote.
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.PARAGRAPH
        self.assertEqual(actual, expected)

    def test_quote_no_space(self):
        text = """
>this is a quote.
>who am i quoting?
>who cares you just need to know this is a quote.
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.QUOTE
        self.assertEqual(actual, expected)

    def test_unordered_list(self):
        text = """
- this is an unordered list
- you can list all the things in an unordered way
- who needs numbers
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.UNORDERED_LIST
        self.assertEqual(actual, expected)

    def test_unordered_list_no_space(self):
        text = """
    -this is an unordered list
    -you can list all the things in an unordered way
    -who needs numbers
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.PARAGRAPH
        self.assertEqual(actual, expected)

    def test_unordered_list_partial(self):
        text = """
    - this is an unordered list
    you can list all the things in an unordered way
    - who needs numbers
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.PARAGRAPH
        self.assertEqual(actual, expected)

    def test_unordered_list_oneline(self):
        text = """
- this is an unordered list
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.UNORDERED_LIST
        self.assertEqual(actual, expected)

    def test_ordered_list(self):
        text = """
1.thing1
2.thing2
3.thing3
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.ORDERED_LIST
        self.assertEqual(actual, expected)

    def test_ordered_list_wrong_numbers(self):
        text = """
2.thing1
1.thing2
3.thing3
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.PARAGRAPH
        self.assertEqual(actual, expected)

    def test_ordered_list_no_period(self):
        text = """
1thing1
2thing2
3thing3
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.PARAGRAPH
        self.assertEqual(actual, expected)

    def test_ordered_list_partial(self):
        text = """
1.thing1
2.thing2
thing3
        """
        actual = block_to_block_type(markdown_to_blocks(text)[0])
        expected = BlockType.PARAGRAPH
        self.assertEqual(actual, expected)

    def test_combined(self):
        text = """
### this is the heading

```
there is some code here too```

> we also have a quote

- cant forget an unordered list

1. very important ordered list

also normal paragraph
        """
        actual = []
        for block in markdown_to_blocks(text):
            actual.append(block_to_block_type(block))
        expected = [
            BlockType.HEADING,
            BlockType.CODE,
            BlockType.QUOTE,
            BlockType.UNORDERED_LIST,
            BlockType.ORDERED_LIST,
            BlockType.PARAGRAPH
        ]
        self.assertEqual(actual, expected)
