from textnode import *
from htmlnode import *
from extract_links import *
import re

def text_to_textnodes(text):
     new_nodes = []

     new_nodes.extend(split_nodes_delimiter([text], "**", TextType.BOLD))

     new_nodes = (split_nodes_delimiter(new_nodes, "_", TextType.ITALIC))

     new_nodes = (split_nodes_delimiter(new_nodes, "`", TextType.CODE))

     new_nodes = (split_nodes_images(new_nodes))

     new_nodes = (split_nodes_links(new_nodes))

     return new_nodes
# node = TextNode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", TextType.TEXT)

# result = text_to_textnodes(node)
# print(result)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
     new_nodes = []
     for old_node in old_nodes:
          if old_node.text_type != TextType.TEXT:
               new_nodes.append(old_node)
               continue

          words = old_node.text.split(delimiter)
          if len(words)%2 == 0:
               raise Exception("Invalid Markdown syntax")
          
          # "just text" ->["just text"]
          # "text **bold** more" -> ["text ", "bold", " more"]
          # "**a** and **b**" -> ["", "a", "", " and ", "", "b", ""]

          nodes = []
          for i, word in enumerate(words):
               if word == '':
                    continue
               if i%2 == 0:
                    nodes.append(TextNode(word, TextType.TEXT))
               else:
                    nodes.append(TextNode(word, text_type))
          
          new_nodes.extend(nodes)
     return new_nodes

def split_nodes_images(old_nodes):
     new_nodes = []
     for old_node in old_nodes:
          # if not TextType.TEXT, extend as it is and iterate to next
          if old_node.text_type != TextType.TEXT:
               new_nodes.append(old_node)
               continue

          images = extract_markdown_images(old_node.text)
          
          # if no images found, extend the old_node as it is and iterate to the next
          if not images:
               new_nodes.append(old_node)
               continue

          nodes = []
          node_str = old_node.text
          for img in images:
               split = node_str.split(f"![{img[0]}]({img[1]})")
               if split[0] != '':
                    nodes.append(TextNode(split[0], TextType.TEXT))
               nodes.append(TextNode(img[0], TextType.IMAGE, img[1]))
               
               node_str = split[1]

          # if there is node_str left than extend it to the list
          if node_str:
               nodes.append(TextNode(node_str, TextType.TEXT))
          new_nodes.extend(nodes)

     return new_nodes
               
def split_nodes_links(old_nodes):
     new_nodes = []

     for old_node in old_nodes:
          # if not TextType.TEXT, extend as it is and iterate to next
          if old_node.text_type != TextType.TEXT:
               new_nodes.append(old_node)
               continue

          links = extract_markdown_links(old_node.text)
          
          # if no links found, extend the old_node as it is and iterate to the next
          if not links:
               new_nodes.append(old_node)
               continue

          nodes = []
          node_str = old_node.text
          for link in links:
               split = node_str.split(f"[{link[0]}]({link[1]})")

               if split[0] != '':
                    nodes.append(TextNode(split[0], TextType.TEXT))
               nodes.append(TextNode(link[0], TextType.LINK, link[1]))
               
               node_str = split[1]
          
          # if there is node_str left than extend it to the list
          if node_str:
               nodes.append(TextNode(node_str, TextType.TEXT))
          new_nodes.extend(nodes)
     return new_nodes

#  *****sample tests below*****

# img_text = TextNode(
#     "This is image with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
#     TextType.TEXT,
# )
# link = TextNode(
#     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#     TextType.TEXT,
# )
# print(split_nodes_images([img_text]))
# print(split_nodes_links([link]))


def extract_markdown_images(img_text):
     pattern = r"(?<=!)\[([^\[\]]*)\]\(([^\[\]]*)\)"
     #              "[^\[\]]*"
     # the above component has the initial [] which character class with ^ indicating to ignore the following letters 
     # letters/chr to ignore is "[" and "]" and followed by * at the end of the bracket for chr class meaning 0 or more of the allowed chrs 
     return re.findall(pattern, img_text)

def extract_markdown_links(text):
     pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\[\]]*)\)"
     return re.findall(pattern, text)

