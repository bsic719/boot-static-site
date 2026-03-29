import unittest

from textnode import TextNode, TextType

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


if __name__ == "__main__":
     unittest.main()