class HTMLNode():
     def __init__(self, tag=None, value=None, children=None, props=None):
          self.tag = tag
          self.value = value
          self.children = children
          self.props = props

     def to_html(self):
          raise NotImplementedError
     
     def props_to_html(self):
          if self.props == None:
               return ''

          props_html = ""
          for prop in self.props:
               props_html += f' {prop}="{self.props[prop]}"'
          return props_html
          # return f' {self.props['href']} {self.props['target']}'
     
     def __repr__(self):
          return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
     
     def __eq__(self, other):
          return(
               self.tag == other.tag and
               self.value == other.value and
               self.children == other.children and
               self.props == other.props
          )

class LeafNode(HTMLNode):
     def __init__(self, tag=None, value=None, props=None):
          super().__init__(tag, value, None, props)
     
     def to_html(self):
          if self.value == None:
               raise ValueError
          if self.tag == None:
               return self.value
          
          if self.props == None:
               return f"<{self.tag}>{self.value}</{self.tag}>"
          else:
               return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
     
     def __repr__(self):
          return f"LeafNode({self.tag}, {self.value}, {self.props})"
