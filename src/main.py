from textnode import TextNode, TextType


def main():
     print(TextNode('This is some anchor text', TextType('link'), 'https://www.boot.dev'))
     print(TextNode('THIS IS BOLD TEXTS', TextType('bold')))
     print(TextNode('print("Hi")', TextType('code')))
     print(TextNode('some random texts that doesn"t mean anything', TextType('text')))

main()