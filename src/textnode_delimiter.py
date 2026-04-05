from textnode import *
from htmlnode import *

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

