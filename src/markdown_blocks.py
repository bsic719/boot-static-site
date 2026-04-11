from enum import Enum
import re

# surpported markdown blocks
# paragraph
# heading
# code
# quote
# unordered_list
# ordered_list
def markdown_to_blocks(markdown):
     blocks = markdown.split("\n\n")
     filtered_blocks = []

     for block in blocks:
          if block == '':
               continue
          block = block.strip()
          filtered_blocks.append(block)
     return filtered_blocks

class BlockType(Enum):
     PARAGRAPH = 'paragraph'
     HEADING = 'heading'
     CODE = 'code'
     QUOTE = 'quote'
     ULIST = 'unordered_list'
     OLIST = 'ordered_list'

def block_to_blocktype(block):
     headings_pattern = r"^#{1,6}\s(.+)$"
     # ^ is start of the line
     # .{1,6} matches any 1 to 6 characters
     # \s matches a single space
     # (.+) captures heading text
     # $ end of the line
     code_pattern = r"^```\n.+\n```$"
     quote_pattern = r"^>.+$"
     unordered_list = r"^-\s{1}\w{1}.+$"
     ordered_list = r"^\d+\.\s\w{1}.+$"

     if re.match(headings_pattern, block):
          return BlockType.HEADING
     if re.match(code_pattern, block):
          return BlockType.CODE

     block_split = block.split('\n')
     for i, line in enumerate(block_split):
          if re.match(quote_pattern, line):
               if i+1 == len(block_split):
                    return BlockType.QUOTE

     for i, line in enumerate(block_split):
          if re.match(unordered_list, line):
               if i+1 == len(block_split):
                    return BlockType.ULIST

     for i, line in enumerate(block_split):
          if re.match(ordered_list, line):
               if i+1 == len(block_split) and int(line[0]) == i+1:
                    return BlockType.OLIST

     return BlockType.PARAGRAPH

msg = '###### Heading 1'
msg2 = "```\ncode block\n```"
msg3 = "> I have a dream\n> That all man will be equal\n>And all will propser"
msg4 = "- eat food\n- poop it out"
msg5 = "1. I have a dream"
msg6 = "2. I have a dream"
block_to_blocktype(msg)
block_to_blocktype(msg2)
block_to_blocktype(msg3)
block_to_blocktype(msg4)
block_to_blocktype(msg5)



