import unittest
from block_markdown import *

class TestBlockSplits(unittest.TestCase):
     def test_multi_blocks(self):
          message = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
          self.assertEqual(
               markdown_to_blocks(message),
               [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
               ]
          )
     
     def test_single_block(self):
          message = "This is a simple paragraph with **bold** statements"
          self.assertEqual(
               markdown_to_blocks(message),
               [
                    "This is a simple paragraph with **bold** statements"
               ]
          )
     
     def test_multi_blocks_multi_newlines(self):
          message = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""       
          self.assertEqual(
               markdown_to_blocks(message),
               [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
               ],
          )