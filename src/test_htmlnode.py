import unittest

from htmlnode import HTMLNode
    
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

if __name__ == "__main__":
    unittest.main()