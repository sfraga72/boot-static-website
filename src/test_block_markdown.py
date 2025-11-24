import unittest

from block_markdown import markdown_to_blocks
from textnode import TextNode, TextType

class TestMarkdownToBlocks(unittest.TestCase):
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

    def test_markdown_to_blocks_newlines(self):
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

    def test_empty_markdown(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])
    
    def test_single_paragraph(self):
        md = "This is a single paragraph without any special formatting."
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a single paragraph without any special formatting."])
    
    def test_code_block(self):
        md = """
Here is a code block:
`
def hello_world():
    print("Hello, world!")
`
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Here is a code block:\n`\ndef hello_world():\n    print(\"Hello, world!\")\n`"
            ],
        )
    

if __name__ == "__main__":
    unittest.main()