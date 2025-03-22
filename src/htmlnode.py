

class HTMLNode():
	def __init__(self,tag = None,value = None,children = None,props = None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError
	
	def props_to_html(self):
		my_string = ""
		if self.props is not None:
			for key, value in self.props.items():
				my_string += f' {key}="{value}"'
		return my_string
	
	def __repr__(self):
		
		return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props}"
	

