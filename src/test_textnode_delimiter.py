import unittest
from textnode import *
from htmlnode import *
from textnode_delimiter import *

class TestDelimiter(unittest.TestCase):
     bold_node = TextNode("This is text with a **bold** word", TextType.TEXT)
     bold_node2 = TextNode("This is **something** special, do you **understand** corporal?", TextType.TEXT)
     italic_node = TextNode("This is text with an _italic_ word", TextType.TEXT)
     code_node = TextNode("This is text with a `code block` word", TextType.TEXT)
     code_node2 = TextNode("This is text with a `code block`", TextType.TEXT)
     error_node = TextNode("This is a normal **block of text", TextType.TEXT)
     def test_bold(self):
          new_nodes = split_nodes_delimiter([self.bold_node], "**", TextType.BOLD)

          self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" word", TextType.TEXT)])
     
     def test_bold2(self):
          new_nodes = split_nodes_delimiter([self.bold_node, self.italic_node, self.code_node], "**", TextType.BOLD)

          self.assertEqual(
               new_nodes, 
               [
                    TextNode("This is text with a ", TextType.TEXT), 
                    TextNode("bold", TextType.BOLD), 
                    TextNode(" word", TextType.TEXT), 
                    TextNode("This is text with an _italic_ word", TextType.TEXT), 
                    TextNode("This is text with a `code block` word", TextType.TEXT)])
     
     def test_multi_bold(self):
          new_nodes = split_nodes_delimiter([self.bold_node2], "**", TextType.BOLD)

          self.assertEqual(
               new_nodes,
               [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("something", TextType.BOLD),
                    TextNode(" special, do you ", TextType.TEXT),
                    TextNode("understand", TextType.BOLD),
                    TextNode(" corporal?", TextType.TEXT)
               ]
          )
     
     def test_italic(self):
          new_nodes = split_nodes_delimiter([self.bold_node, self.italic_node, self.code_node], "_", TextType.ITALIC)

          self.assertEqual(
               new_nodes, 
               [
                    TextNode("This is text with a **bold** word", TextType.TEXT), 
                    TextNode("This is text with an ", TextType.TEXT), 
                    TextNode("italic", TextType.ITALIC), 
                    TextNode(" word", TextType.TEXT), 
                    TextNode("This is text with a `code block` word", TextType.TEXT)])
     
     def test_code(self):
          new_nodes = split_nodes_delimiter([self.bold_node, self.italic_node, self.code_node2], "`", TextType.CODE)

          self.assertEqual(
               new_nodes, 
               [
                    TextNode("This is text with a **bold** word", TextType.TEXT), 
                    TextNode("This is text with an _italic_ word", TextType.TEXT), 
                    TextNode("This is text with a ", TextType.TEXT), 
                    TextNode("code block", TextType.CODE)
               ]
          )
     
     def test_Exception(self):
          with self.assertRaises(Exception) as err:

               new_nodes = split_nodes_delimiter([error_node], "**", TextType.BOLD)

               self.assertEqual(str(err.exception), "Invalid Markdown syntax")
