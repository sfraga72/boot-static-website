import unittest

from gencontent import extract_title

class TestGenContent(unittest.TestCase):
    def test_extract_title(self):
        md_with_title = """# My Title
This is some content.
- A list item
- Another item
"""
        title = extract_title(md_with_title)
        self.assertEqual(title, "My Title")
    
    def test_extract_title_no_title(self):
        md_without_title = """This is some content without a title.
- A list item
- Another item
"""
        with self.assertRaises(ValueError) as context:
            extract_title(md_without_title)
        self.assertEqual(str(context.exception), "No title found in markdown")
    
    def test_extract_title_multiple_titles(self):
        md_multiple_titles = """# First Title
Some content here.
# Second Title
More content.
"""
        title = extract_title(md_multiple_titles)
        self.assertEqual(title, "First Title")      

    def test_extract_title_title_with_whitespace(self):
        md_with_whitespace = """#    Title with Whitespace
Content here.
"""
        title = extract_title(md_with_whitespace)
        self.assertEqual(title, "Title with Whitespace")

    def test_extract_title_empty_markdown(self):
        empty_md = ""
        with self.assertRaises(ValueError) as context:
            extract_title(empty_md)
        self.assertEqual(str(context.exception), "No title found in markdown")  
    
    def test_extract_title_not_subtitle(self):
        md_with_subtitle = """## Subtitle Here
Content here.
"""
        with self.assertRaises(ValueError) as context:
            extract_title(md_with_subtitle)
        self.assertEqual(str(context.exception), "No title found in markdown")
    
    def test_extract_title_title_and_subtitle(self):
        md_with_title_and_subtitle = """# Main Title
Some content.
## Subtitle Here
More content.
"""
        title = extract_title(md_with_title_and_subtitle)
        self.assertEqual(title, "Main Title")

if __name__ == "__main__":
    unittest.main()