import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
     # node = HTMLNode('p', 'This is a text paragraph')
     # node2 = HTMLNode('p', 'This is a text paragraph')
     # node3 = HTMLNode('h1', 'This is a header', [node])
     # node4 = HTMLNode('h2', 'This is a header', [node])
     # node5 = HTMLNode('a', 'This is a hyperlink', [node], {"href": "https://www.google.com"})
     # node6 = HTMLNode('a', 'This is a hyperlink', [node], {"href": "https://www.google.com"})
     # node7 = HTMLNode('a', 'This is a hyperlink', [node], {"href": "https://www.boots.com"})

     # def test_eq(self):
     #      self.assertEqual(self.node, self.node2)

     # def test_eq2(self):
     #      self.assertEqual(self.node5, self.node6)
     
     # def test_eq_false(self):
     #      self.assertNotEqual(self.node3, self.node4)

     # def test_eq_false2(self):
     #      self.assertNotEqual(self.node3, self.node4)

     # def test_eq_false3(self):
     #      self.assertNotEqual(self.node6, self.node7)

     # def test_repr(self):
     #      self.assertEqual(
     #           "HTMLNode(a, This is a hyperlink, [HTMLNode(p, This is a text paragraph, None, None)], {'href': 'https://www.boots.com'})", repr(self.node7)
     #      )
     ######################################
     def test_to_html_propr(self):
          node = HTMLNode(
               "div", 
               "Hello, world!", 
               None,
               {"class": "greeting", "href": "https://boot.dev"},
          )
          self.assertEqual(
               node.props_to_html(),
               ' class="greeting" href="https://boot.dev"'
          )

     def test_values(self):
          node = HTMLNode(
               'div', 
               'I wish i could read'
          )
          self.assertEqual(node.tag, 'div')
          self.assertEqual(node.value, 'I wish i could read')
          self.assertEqual(node.children, None)
          self.assertEqual(node.props, None)
     
     def test_repr(self):
          node = HTMLNode(
               'p', 
               'What a strange world',
               None,
               {"class": "primary"},
          )
          self.assertEqual(
               node.__repr__(),
               "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})"
               )
if __name__ == '__main__':
     unittest.main()