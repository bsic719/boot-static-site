import unittest

from htmlnode import HTMLNode, LeafNode

class TestLeafNode(unittest.TestCase):
     def test_leaf_to_html_p(self):
          node = LeafNode("p", "This is a paragraph of text.")
          self.assertEqual(
               node.to_html(), "<p>This is a paragraph of text.</p>"
          )
     
     def test_leaf_to_html_a(self):
          node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
          self.assertEqual(
               node.to_html(), '<a href="https://www.google.com">Click me!</a>'
          )

     def test_leaf_to_html_no_tag(self):
          node = LeafNode(None, "No tag paragraph!")
          self.assertEqual(
               node.to_html(), "No tag paragraph!"
          )
          
     def test_repr(self):
          node = LeafNode("p", "Hello, world!")
          self.assertEqual(
               repr(node), "LeafNode(p, Hello, world!, None)"
          )

if __name__ == '__main__':
     unittest.main()
