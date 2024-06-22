import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = TextNode("What in sam hill?!", "italic", "www.hero.alliance")
        node2 = TextNode("What in sam hill?!", "italic", "www.hero.alliance")
        self.assertEqual(node, node2)
    def test_eq3(self):
        node = TextNode("Show me the money!", "bold", None)
        node2 = TextNode("Show me the money!", "bold", None)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()