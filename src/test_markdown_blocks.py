import unittest
from markdown_blocks import *

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

class TestBlockToBlockType(unittest.TestCase):
     def test_heading(self):
          block = '###### Heading 1'
          self.assertEqual(
               block_to_blocktype(block),
               BlockType.HEADING
          )
     
     def test_code(self):
          block = "```\ncode block\n```"
          self.assertEqual(
               block_to_blocktype(block),
               BlockType.CODE
          )

     def test_quote(self):
          block = "> I have a dream\n> That all man will be equal\n>And all will propser"
          self.assertEqual(
               block_to_blocktype(block),
               BlockType.QUOTE
          )

     def test_Ulist(self):
          block = "- eat food\n- poop it out"
          self.assertEqual(
               block_to_blocktype(block),
               BlockType.ULIST
          )

     def test_Olist(self):
          block = "1. Wake up\n2. Pee\n3. Make coffee"
          self.assertEqual(
               block_to_blocktype(block),
               BlockType.OLIST
          )

     def test_Olist_error(self):
          block = "2.Pee"
          self.assertEqual(
               block_to_blocktype(block),
               BlockType.PARAGRAPH
          )
          
     def test_paragraph(self):
          block = "This is the first sentence in the paragraph\nThis is the second sentence\n1. Make coffee"
          self.assertEqual(
               block_to_blocktype(block),
               BlockType.PARAGRAPH
          )
     
