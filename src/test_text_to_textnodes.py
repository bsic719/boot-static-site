import unittest
from text_to_textnodes import *

class TestTextToTextNodes(unittest.TestCase):
     def test_multiple_types(self):
          node = TextNode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", TextType.TEXT)

          self.assertEqual(
               text_to_textnodes(node),
               [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),
               ]
          ) 
     
     def test_text_to_textnodes_plain(self):
          node = TextNode("Just plain text", TextType.TEXT)

          self.assertEqual(
               text_to_textnodes(node),
               [
                  TextNode("Just plain text", TextType.TEXT)  
               ]
          )