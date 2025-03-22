from enum import Enum
import re
from parentnode import ParentNode
from htmlnode import HTMLNode
from textnode import text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


# def block_to_block_type(markdown):

#     if re.findall(r"^#{1,6} .+",markdown):
#         return BlockType.HEADING
#     if re.findall(r"^```(\n|.)+```$",markdown):
#         return BlockType.CODE
#     splitted = markdown.split("\n")
#     all_match = True
#     for line in splitted:
#         if not re.findall(r"^- ",markdown):
#             all_match = False
#         if all_match:
#             return BlockType.ULIST
#     all_match = True
#     for line in splitted:
#         if not re.findall(r"^>",markdown):
#             all_match = False
#         if all_match:
#             return BlockType.QUOTE
#     all_match = True
#     if markdown.startswith("1. "):
#         i = 1
#         for line in splitted:
#             if not line.startswith(f"{i}. "):
#                 return BlockType.PARAGRAPH
#             i += 1
#         return BlockType.OLIST
#     return BlockType.PARAGRAPH

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                html_node = HTMLNode("p",block)
            case BlockType.HEADING:
                html_node = HTMLNode("h1",block)
            case BlockType.CODE:
                HTMLNode("code",block,None,)
            case BlockType.QUOTE:
                pass
            case BlockType.QLIST:
                pass
            case BlockType.ULIST:
                pass


def text_to_children(text):
    pass