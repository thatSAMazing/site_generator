import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
		
	def test_leaf_to_html_a(self):
		node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com","target": "_blank",})
		self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Hello, world!</a>')

	def test_leaf_to_html_div(self):
		node = LeafNode("div", "Hello, world!", {"href": "https://www.google.com","target": "_blank",})
		self.assertEqual(node.to_html(), '<div href="https://www.google.com" target="_blank">Hello, world!</div>')