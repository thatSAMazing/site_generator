from textnode import TextType, TextNode
import os
import shutil



def source_to_destination(source,destination):
	if os.path.exists(destination):
		shutil.rmtree(destination)
	if not os.path.isfile(source):
		os.mkdir(destination)
	items_in_source = os.listdir(source)
	for item in items_in_source:
		if os.path.isfile(f"{source}/{item}"):
			new_source = f"{source}/{item}"
			new_destination = f"{destination}/{item}"			
			shutil.copy(new_source,new_destination)
		else:
			new_source = f"{source}/{item}"
			new_destination = f"{destination}/{item}"
			source_to_destination(new_source,new_destination)
	
	


def main():
	source_to_destination("static","public")
	#git test


if __name__ == "__main__":
	main()