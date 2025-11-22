import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_to_html_not_implemented(self):
        node = HTMLNode(tag="div")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html_no_props(self):
        node = HTMLNode(tag="div")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_props(self):
        node = HTMLNode(tag="div", props={"class": "container", "id": "main"})
        expected_html = ' class="container" id="main"'
        self.assertEqual(node.props_to_html(), expected_html)

    def test_repr(self):
        node = HTMLNode(tag="p", value="Hello", children=[], props={"style": "color:red;"})
        expected_repr = "HTMLNode(tag=p, value=Hello, children=[], props={'style': 'color:red;'})"
        self.assertEqual(repr(node), expected_repr)
