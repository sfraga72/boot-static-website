import unittest
from htmlnode import HTMLNode, LeafNode

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_span_with_props(self):
        node = LeafNode("span", "Important", props={"class": "highlight"})
        self.assertEqual(node.to_html(), '<span class="highlight">Important</span>')
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
