from textnode import *
from htmlnode import *
from textnode_delimiter import *

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
