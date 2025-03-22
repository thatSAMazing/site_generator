import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
	def test_eq(self):
		node = HTMLNode("p", "the value",["a","h1","p"],{"href": "https://www.google.com","target": "_blank",})
		node2 = HTMLNode("p", "the value",["a","h1","p"],{"href": "https://www.google.com","target": "_blank",})
		self.assertEqual(node.tag, node2.tag)
		self.assertEqual(node.value, node2.value)
		self.assertEqual(node.children, node2.children)
		self.assertEqual(node.props, node2.props)

	def test_not_eq(self):
		node = HTMLNode("a", "the value",["a","h1","p"],{"href": "https://www.google.com","target": "_blank",})
		node2 = HTMLNode("p", "the value",["a","h1","p"],{"href": "https://www.google.com","target": "_blank",})
		self.assertNotEqual(node, node2)

	def test_props_to_html(self):
		node = HTMLNode("a", "the value",["a","h1","p"],{"href":"https://www.google.com","target":"_blank",})
		returned = node.props_to_html()
		self.assertEqual(returned,  ' href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()