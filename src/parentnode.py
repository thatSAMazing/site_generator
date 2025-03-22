from htmlnode import HTMLNode

class ParentNode(HTMLNode):
	def __init__(self, tag, children,props=None):
		super().__init__(tag,None,children,props)

	def to_html(self):
		if self.tag is None:
			raise ValueError("tag cannot be None")
		if self.children is None:
			raise ValueError("Parent nodes must have children")
		my_string = ""
		for node in self.children:
			my_string += f'<{self.tag}>{self.props_to_html()}{node.to_html()}</{self.tag}>'
			return my_string

	def __repr__(self):
			return f"ParentNode({self.tag}, children: {self.children}, {self.props})"