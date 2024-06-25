import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
    
class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        test = HTMLNode("p", "Which way western man?", None, {"id": "Test","onclick": "true"})
        self.assertEqual(test.props_to_html(), ' id="Test" onclick="true"')
    def test_props2(self):
        test = HTMLNode("h2", "There was a tapping...", None, {"id": "Tapper","onclick": "tap()"})
        self.assertEqual(test.props_to_html(), ' id="Tapper" onclick="tap()"')
    def test_props3(self):
        test = HTMLNode(None, None, None, None)
        self.assertEqual(test.props_to_html(), '')

    def test_to_html_no_children(self):
        test = LeafNode("p", "Im a leaf on the wind")
        self.assertEqual(test.to_html(), '<p>Im a leaf on the wind</p>')
    def test_to_html_no_tag(self):
        test = LeafNode(None, "Leafy bits")
        self.assertEqual(test.to_html(), "Leafy bits")

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )
    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
if __name__ == "__main__":
    unittest.main()