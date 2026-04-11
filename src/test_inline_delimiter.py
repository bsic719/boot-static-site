import unittest
from textnode import *
from htmlnode import *
from inline_delimiter import *

class TestInlineMarkdown(unittest.TestCase):
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

     ######################################
     # Below are Tests for images and links
     ######################################
     def test_images(self):
          node = TextNode("This is image with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT,)

          self.assertEqual(
               split_nodes_images([node]),
               [
                    TextNode("This is image with a ", TextType.TEXT),
                    TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                    TextNode(" and ", TextType.TEXT),
                    TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
               ]
          )

     def test_links(self):
          node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT,)

          self.assertEqual(
               split_nodes_links([node]),
               [
                    TextNode("This is text with a link ", TextType.TEXT),
                    TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                    TextNode(" and ", TextType.TEXT),
                    TextNode("to youtube", TextType.LINK,'https://www.youtube.com/@bootdotdev')
               ]
          )
     
     def test_split_link_with_image(self):
          node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT,)
     
          self.assertEqual(
               split_nodes_images([node]),
               [
                    TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
               ]
          )
     
     def test_links_and_images(self):
          img_node = TextNode("This is image with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT,)
          link_node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT,)

          self.assertEqual(
               split_nodes_links([img_node, link_node]),
               [
                    TextNode("This is image with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT),
                    TextNode("This is text with a link ", TextType.TEXT),
                    TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                    TextNode(" and ", TextType.TEXT),
                    TextNode("to youtube", TextType.LINK,'https://www.youtube.com/@bootdotdev'),
               ]
          )



     ######################################
     # extract links & images
     ######################################
class TestExtractLinks(unittest.TestCase):
     def test_extract_link(self):
          text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
          
          self.assertEqual(
               extract_markdown_links(text),
               [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
          )
     
     def test_extract_img(self):
          img_text = "This is image with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

          self.assertEqual(
               extract_markdown_images(img_text),
               [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
          ) 
     
     def test_extract_img_on_link(self):
          text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
          
          self.assertEqual(
               extract_markdown_images(text),
               []
          )


     ######################################
     # Converting text to TextNodes
     ######################################
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
