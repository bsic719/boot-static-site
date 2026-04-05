from enum import Enum
from htmlnode import *

class TextType(Enum):
     TEXT = 'text'
     BOLD = 'bold'
     ITALIC = 'italic'
     CODE = 'code'
     LINK = 'link'
     IMAGE = 'image'

     # 'texttype.value' equals the 'variable name'
     # 'texttype' equals the 'value'

class TextNode():
     def __init__(self, text, text_type, url=None):
          self.text = text
          self.text_type = text_type 
          self.url = url
     
     def __eq__(self, other):
          text_equal = self.text == other.text
          text_type_equal = self.text_type == other.text_type
          url_equal = self.url == other.url

          return text_equal and text_type_equal and url_equal
     
     def __repr__(self):
          return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
     tag = text_node.text_type
     if tag == TextType.TEXT:
          return LeafNode(None, text_node.text)
     if tag == TextType.BOLD:
          return LeafNode("b" , text_node.text)
     if tag == TextType.ITALIC:
          return LeafNode("i", text_node.text)
     if tag == TextType.CODE:
          return LeafNode("code", text_node.text)
     if tag == TextType.LINK:
          return LeafNode("a", text_node.text, {"href": text_node.url})
     if tag == TextType.IMAGE:
          return LeafNode(
               "img", 
               "", 
               {
                    "src": text_node.url,
                    "alt": "This is an image",
               }
          )
     
     raise Exception("Not a valid TextType")
