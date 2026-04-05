import unittest
from textnode import *
# import htmlnode
# from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
     def test_eq(self):
          node = TextNode('This is a text node', TextType.BOLD)
          node2 = TextNode('This is a text node', TextType.BOLD)
          self.assertEqual(node, node2)
     
     def test_eq_url(self):
          node = TextNode("This is a text node", TextType.ITALIC, 'https://images.google.com/')
          node2 = TextNode("This is a text node", TextType.BOLD, 'https://images.google.com/')
          self.assertEqual(node.url, node2.url)

     def test_eq_false(self):
          node = TextNode("This is a text node", TextType.ITALIC)
          node2 = TextNode("This is a text node", TextType.BOLD)
          self.assertNotEqual(node, node2)

     def test_eq_false2(self):
          node = TextNode("This is a text node", TextType.LINK, 'https://images.google.com/')
          node2 = TextNode("This is a text node", TextType.BOLD)
          self.assertNotEqual(node, node2)
     
     def test_repr(self):
          node = TextNode("This is a text node", TextType.TEXT, 'https://www.boot.dev')
          self.assertEqual(
               'TextNode(This is a text node, text, https://www.boot.dev)', repr(node)
               )
     # ###### Testing text_node_to_html_node()
     def test_text(self):
          node = TextNode("This is a text node", TextType.TEXT)
          html_node = text_node_to_html_node(node)
          self.assertEqual(html_node.tag, None)
          self.assertEqual(html_node.value, "This is a text node")
     
     def test_text_to_html_and_repr(self):
          node = TextNode("This is a BOLD statement", TextType.BOLD)
          html_node = text_node_to_html_node(node)
          self.assertEqual(html_node.to_html(), "<b>This is a BOLD statement</b>")
          self.assertEqual(repr(html_node), "LeafNode(b, This is a BOLD statement, None)")

     def test_text_img(self):
          node = TextNode("", TextType.IMAGE, "https://www.boot.dev")
          html_node = text_node_to_html_node(node)
          self.assertEqual(html_node.props, {"src": "https://www.boot.dev", "alt": "This is an image"})
          # self.assertEqual(html_node.to_html(), '<img src="https://www.boot.dev" alt="This is an image"></img>')
if __name__ == "__main__":
     unittest.main()