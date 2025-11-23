import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_leaf_repr(self):
        node = LeafNode("a", "Link", props={"href": "http://example.com"})
        expected_repr = "LeafNode(a, Link, {'href': 'http://example.com'})"
        self.assertEqual(repr(node), expected_repr)

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
    
    def test_parent_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_parent_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_parent_repr(self):
        child_node = LeafNode("i", "italic")
        parent_node = ParentNode("p", [child_node], props={"class": "text"})
        expected_repr = "ParentNode(p, children: [LeafNode(i, italic, None)], {'class': 'text'})"
        self.assertEqual(repr(parent_node), expected_repr)
    
    def test_parent_to_html_with_props(self):
        child_node = LeafNode("b", "bold text")
        parent_node = ParentNode("div", [child_node], props={"style": "font-weight:bold;"})
        expected_html = '<div style="font-weight:bold;"><b>bold text</b></div>'
        self.assertEqual(parent_node.to_html(), expected_html)
    
    def test_parent_to_html_multiple_children(self):
        child1 = LeafNode("h1", "Title")
        child2 = LeafNode("p", "Paragraph")
        parent_node = ParentNode("section", [child1, child2])
        expected_html = "<section><h1>Title</h1><p>Paragraph</p></section>"
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_parent_to_html_no_children_empty_list(self):
        parent_node = ParentNode("div", [])
        expected_html = "<div></div>"
        self.assertEqual(parent_node.to_html(), expected_html)
    
    def test_leaf_to_html_with_props_empty(self):
        node = LeafNode("p", "Hello, world!", props={})
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_parent_to_html_with_props_empty(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props={})
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_parent_to_html_nested_props(self):
        grandchild_node = LeafNode("i", "italic")
        child_node = ParentNode("span", [grandchild_node], props={"class": "inner"})
        parent_node = ParentNode("div", [child_node], props={"id": "outer"})
        expected_html = '<div id="outer"><span class="inner"><i>italic</i></span></div>'
        self.assertEqual(parent_node.to_html(), expected_html)
    
    def test_parent_to_html_multiple_nested_children(self):
        child1 = LeafNode("h2", "Subtitle")
        grandchild = LeafNode("em", "emphasized text")
        child2 = ParentNode("p", [grandchild])
        parent_node = ParentNode("article", [child1, child2])
        expected_html = "<article><h2>Subtitle</h2><p><em>emphasized text</em></p></article>"
        self.assertEqual(parent_node.to_html(), expected_html)
    
    def test_parent_to_html_with_text_leaf(self):
        text_leaf = LeafNode(None, "Some text")
        parent_node = ParentNode("div", [text_leaf])
        expected_html = "<div>Some text</div>"
        self.assertEqual(parent_node.to_html(), expected_html)
    
    def test_multiple_parent_nested_levels(self):
        level3 = LeafNode("span", "Level 3")
        level2 = ParentNode("div", [level3], props={"class": "level2"})
        level1 = ParentNode("section", [level2], props={"id": "level1"})
        expected_html = '<section id="level1"><div class="level2"><span>Level 3</span></div></section>'
        self.assertEqual(level1.to_html(), expected_html)
    
if __name__ == "__main__": 
    unittest.main()
