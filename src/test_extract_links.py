import unittest
from extract_links import *

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
