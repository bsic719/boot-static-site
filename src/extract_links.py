import re

def extract_markdown_images(img_text):
     pattern = r"!\[([^\[\]]*)\]\(([^\[\]]*)\)"
     #              "[^\[\]]*"
     # the above component has the initial [] which character class with ^ indicating to ignore the following letters 
     # letters/chr to ignore is "[" and "]" and followed by * at the end of the bracket for chr class meaning 0 or more of the allowed chrs 
     return re.findall(pattern, img_text)

def extract_markdown_links(text):
     pattern = r"\[(.*?)\]\((.*?)\)"
     return re.findall(pattern, text)


# img_text = "This is image with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# print(extract_markdown_images(img_text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

# text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
# print(extract_markdown_links(text))
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]